# API Estática Familiar

## 📌 Descripción

La familia "Jackson" necesita una API estática que gestione sus miembros. Esta API permite obtener, agregar y eliminar miembros de la familia sin una base de datos, almacenando la información en memoria.

## 🚀 Cómo comenzar este proyecto

Este proyecto está diseñado para ejecutarse en entornos de desarrollo como [Codespaces](https://4geeks.com/es/lesson/tutorial-de-github-codespaces) o [Gitpod](https://4geeks.com/es/lesson/como-utilizar-gitpod). También puedes clonarlo en tu máquina local con:

```sh
https://github.com/breatheco-de/exercise-family-static-api
```

## 💻 Instalación

1. Instala las dependencias del proyecto:
   ```sh
   pipenv install
   ```
2. Entra dentro del *virtual environment*:
   ```sh
   pipenv shell
   ```
3. Inicia el servidor Flask:
   ```sh
   pipenv run start
   ```

## ✅ Pruebas

Ejecuta las pruebas automatizadas con:
```sh
pipenv run test
```

## 📜 Estructura del Proyecto

El proyecto se compone de los siguientes archivos clave:

- `src/datastructure.py`: Contiene la clase `FamilyStructure` que gestiona los miembros de la familia.
- `src/app.py`: Define los endpoints de la API y la lógica de negocio.
- `src/utils.py`: Genera el sitemap y maneja errores.
- `templates/index.html`: Interfaz HTML para probar la API sin herramientas externas.

## 📡 Endpoints de la API

### 1️⃣ Obtener todos los miembros
- **Método:** `GET /members`
- **Respuesta:**
  ```json
  [
    {
      "id": 1,
      "first_name": "John",
      "age": 33,
      "lucky_numbers": [7, 13, 22]
    }
  ]
  ```

### 2️⃣ Obtener un miembro específico
- **Método:** `GET /member/<int:member_id>`
- **Respuesta:**
  ```json
  {
    "id": 1,
    "first_name": "John",
    "age": 33,
    "lucky_numbers": [7, 13, 22]
  }
  ```

### 3️⃣ Agregar un miembro
- **Método:** `POST /member`
- **Cuerpo de la solicitud:**
  ```json
  {
    "first_name": "Michael",
    "age": 29,
    "lucky_numbers": [8, 12, 23]
  }
  ```
- **Respuesta:**
  ```json
  {
    "id": 4,
    "first_name": "Michael",
    "age": 29,
    "lucky_numbers": [8, 12, 23]
  }
  ```

### 4️⃣ Eliminar un miembro
- **Método:** `DELETE /member/<int:member_id>`
- **Respuesta:**
  ```json
  {
    "done": true
  }
  ```

## 🎯 Requisitos tecnológicos

- Todas las solicitudes y respuestas están en `application/json`.
- Códigos de respuesta:
  - `200`: Éxito.
  - `400`: Error de solicitud.
  - `404`: Recurso no encontrado.
- No se usa una base de datos, los datos se almacenan en memoria.

## 🌎 Interfaz de Pruebas

Para probar la API visualmente, accede a `http://localhost:3000/` y usa la interfaz interactiva en `index.html`.

## 🚀 Contribución

Si deseas mejorar el proyecto, puedes hacer un *fork* y enviar un *pull request*.

¡Disfruta programando! 🚀🔥

## 👨‍💻 **Autor**

- **Desarrollado por JulioRom**
- 📧 **Correo:** [julioandrescampos@gmail.com](mailto:julioandrescampos@gmail.com)
- 🔗 **GitHub:** [https://github.com/JulioRom](https://github.com/JulioRom)