
# Django Ninja API Project

Este proyecto es una API construida con Django y Django Ninja que gestiona elementos (`Items`). La API permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre los elementos. El proyecto está preparado para ejecutarse en un entorno Dockerizado para facilitar la configuración y el despliegue.

## Estructura del Proyecto

### `views.py`

Este archivo define las rutas de la API utilizando `Django Ninja`. Las rutas disponibles son:

- **GET /api/items**: Lista todos los elementos.
- **GET /api/items/{item_id}**: Obtiene los detalles de un elemento específico.
- **POST /api/items**: Crea un nuevo elemento.
- **PUT /api/items/{item_id}**: Actualiza un elemento existente.
- **DELETE /api/items/{item_id}**: Elimina un elemento.

### `urls.py`

Este archivo configura las rutas principales del proyecto Django. Se utiliza `Django Ninja` para definir la ruta base de la API bajo el prefijo `/api/`.

### `schemas.py`

Define los esquemas de datos utilizados por la API. Los esquemas son:

- **ItemSchema**: Define la estructura de los datos para un `Item` existente (incluye el campo `id`).
- **ItemCreateSchema**: Define la estructura de los datos requeridos para crear un nuevo `Item`.

### `models.py`

Este archivo define el modelo de datos para los `Items`, que incluye:

- **name**: Un campo de tipo `CharField` que almacena el nombre del ítem (máximo 100 caracteres).
- **description**: Un campo de tipo `TextField` que almacena una descripción del ítem.

### `Dockerfile`

El Dockerfile define el entorno para ejecutar la aplicación. Realiza las siguientes tareas:

- Usa una imagen base de Python 3.9 slim.
- Establece el directorio de trabajo en `/app`.
- Copia el archivo `requirements.txt` y luego instala las dependencias listadas.
- Copia el contenido del proyecto dentro del contenedor.
- Ejecuta las migraciones y levanta el servidor de desarrollo en la dirección `0.0.0.0:8000`.

## Configuración e Instalación

### Prerrequisitos

- Docker y Docker Compose instalados en tu máquina.
- Opcional: Python 3.9 si deseas ejecutar la aplicación localmente sin Docker.

### Instrucciones para Ejecutar con Docker

1. Clona el repositorio:

    ```bash
    git clone https://github.com/DiegoLerma/django.git
    cd django
    ```

2. Construye la imagen de Docker:

    ```bash
    docker build -t django-ninja-api .
    ```

3. Corre el contenedor:

    ```bash
    docker run -p 8000:8000 django-ninja-api
    ```

4. La API estará disponible en `http://localhost:8000/api/`.

### Instrucciones para Ejecutar Localmente (sin Docker)

1. Clona el repositorio y navega al directorio del proyecto:

    ```bash
    git clone https://github.com/DiegoLerma/django.git
    cd django
    ```

2. Crea un entorno virtual e instala las dependencias:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Realiza las migraciones y corre el servidor:

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

4. La API estará disponible en `http://localhost:8000/api/`.

## Uso de la API

### Endpoints Disponibles

- **GET /api/items**: Retorna una lista de todos los elementos.
- **GET /api/items/{item_id}**: Retorna los detalles de un elemento específico por su ID.
- **POST /api/items**: Crea un nuevo elemento. Ejemplo de payload:

    ```json
    {
        "name": "Item 1",
        "description": "Descripción del Item 1"
    }
    ```

- **PUT /api/items/{item_id}**: Actualiza un elemento existente. Ejemplo de payload:

    ```json
    {
        "name": "Item actualizado",
        "description": "Descripción actualizada"
    }
    ```

- **DELETE /api/items/{item_id}**: Elimina un elemento por su ID.

### Ejemplo de Uso con `curl`

Para listar todos los items:

```bash
curl -X GET http://localhost:8000/api/items
```

Para crear un nuevo item:

```bash
curl -X POST http://localhost:8000/api/items -H "Content-Type: application/json" -d '{"name": "Nuevo Item", "description": "Descripción del nuevo Item"}'
```

## Testing

Por defecto, este proyecto incluye los tests básicos para asegurar que las funcionalidades de la API funcionan correctamente. Puedes correr los tests usando:

```bash
python manage.py test
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue el flujo de trabajo de Git estándar:

1. Haz un fork del proyecto.
2. Crea una rama para tu nueva funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza los cambios necesarios y agrega commits descriptivos.
4. Envía un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

Para cualquier pregunta o comentario, puedes abrir un issue en este repositorio o contactarme a través de [tu correo electrónico o sitio web].
