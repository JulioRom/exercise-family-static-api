import pytest, os, sys, tempfile, mock, json
from flask import Flask

@pytest.fixture
def client():
    with mock.patch('flask.Flask', lambda *args, **kwargs: Flask(*args, **kwargs)):
        from app import app, jackson_family
        db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True

        # Reiniciar la estructura de datos antes de cada prueba
        jackson_family._members = [
            {"id": 1, "first_name": "John", "last_name": "Jackson", "age": 33, "lucky_numbers": [7, 13, 22]},
            {"id": 2, "first_name": "Jane", "last_name": "Jackson", "age": 35, "lucky_numbers": [10, 14, 3]},
            {"id": 3, "first_name": "Jimmy", "last_name": "Jackson", "age": 5, "lucky_numbers": [1]}
        ]
        jackson_family._next_id = 4  # Reiniciar el contador de IDs

        with app.test_client() as client:
            yield client

        os.close(db_fd)
        os.unlink(app.config['DATABASE'])


@pytest.mark.it("The Family structure should be initialized with 3 members")
def test_initial_members(client):
    response = client.get('/members')
    members = json.loads(response.data)
    assert len(members) == 3

@pytest.mark.it("POST /member should add a new member")
def test_add_member(client):
    response = client.post('/member', json={
        "first_name": "Tommy",
        "age": 23,
        "lucky_numbers": [34, 65, 23, 4, 6]
    })
    assert response.status_code == 201

@pytest.mark.it("POST /member should return a non-empty response")
def test_add_member_response(client):
    response = client.post('/member', json={
        "first_name": "Sandra",
        "age": 12,
        "lucky_numbers": [12, 34, 33, 45, 32, 12]
    })
    assert response.data != b""

@pytest.mark.it("GET /members should return a list")
def test_get_members(client):
    response = client.get('/members')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

@pytest.mark.it("Adding two members then calling GET /members should return a list with 5 members")
def test_get_members_after_addition(client):
    client.post('/member', json={"first_name": "Tommy", "age": 23, "lucky_numbers": [34, 65, 23]})
    client.post('/member', json={"first_name": "Lily", "age": 30, "lucky_numbers": [5, 10, 15]})
    response = client.get('/members')
    members = json.loads(response.data)
    assert len(members) == 5

@pytest.mark.it("GET /member/<int:id> should return a single family member in dictionary format")
def test_get_member(client):
    response = client.get('/member/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, dict)

@pytest.mark.it("GET /member/<int:id> should contain keys: first_name, id, age, lucky_numbers")
def test_get_member_keys(client):
    response = client.get('/member/1')
    data = json.loads(response.data)
    assert "first_name" in data
    assert "id" in data
    assert "age" in data
    assert "lucky_numbers" in data

@pytest.mark.it("DELETE /member/<int:id> should delete a family member")
def test_delete_member(client):
    client.post('/member', json={"first_name": "Tommy", "age": 23, "lucky_numbers": [34, 65, 23]})
    response = client.delete('/member/4')
    assert response.status_code == 200
    assert response.json["done"] == True

@pytest.mark.it("After deleting a member, GET /members should return a reduced list")
def test_get_members_after_deletion(client):
    response = client.get('/members')
    members = json.loads(response.data)
    assert len(members) == 3