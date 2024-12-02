# Middleware Example

## Requisitos

- Python 3.9+
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)
- [Git](https://git-scm.com/)

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/SosaDevLab/middleware-example.git
   cd middleware-example
   ```

2. Crea un ambiente virtual:

   ```bash
   python -m venv env
   ```

3. Activa el ambiente virtual:

   - En Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecutar el proyecto

Inicia el servidor FastAPI:

```bash
fastapi run app/main.py
```

## Uso del Endpoint

Para usar el endpoint, puedes utilizar cualquier cliente HTTP, como [Postman](https://www.postman.com/) o [Insomnia](https://insomnia.rest/). Asegúrate de enviar los headers necesarios para que el middleware permita el acceso al endpoint.

- **Header:** `X-User`: `SosaDevLab` para que el middleware permita el acceso. Puedes cambiar el valor de `X-User` a cualquier otro valor para probar el middleware.

### Ejemplo de solicitud en Postman/Insomnia

#### Autenticación exitosa

1. Selecciona el método `GET`.
2. Ingresa la URL del endpoint: `http://127.0.0.1:8000/`.
3. En la pestaña de Headers, agrega un nuevo header con la clave `X-User` y el valor `SosaDevLab`.
4. Envía la solicitud y revisa la respuesta.

#### Autenticación fallida

1. Selecciona el método `GET`.
2. Ingresa la URL del endpoint: `http://127.0.0.1:8000/`.
3. En la pestaña de Headers, agrega un nuevo header con la clave `X-User` y el valor `SosaDevLabn't`.
4. Envía la solicitud y revisa la respuesta.
