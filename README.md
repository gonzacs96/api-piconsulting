# api-piconsulting

Para correr este proyecto, sigue los siguientes pasos:

- ENTORNO VIRTUAL

1. Clona el repositorio en tu máquina local.
2. Abre una terminal y navega hasta el directorio del proyecto.
3. Crea un entorno virtual. Puedes hacer esto ejecutando el siguiente comando en la terminal:

   ```
   pip install virtualenv
   ```

   ```
   python -m virtualenv env
   ```

   Desde cmd

   ```
   "env/Scripts/activate"
   ```

   Desde powershell

   ```
   env/Scripts/activate
   ```

   Desde bash

   ```
   source env/Scripts/activate
   ```

4. Instala las dependencias del proyecto usando pip. Puedes hacer esto ejecutando el siguiente comando en la terminal:

   ```
   pip install -r requirements.txt
   ```

5. Inicia el servidor de desarrollo ejecutando el siguiente comando en la terminal:

   ```
   uvicorn main:app --reload
   ```

- CONTENEDOR DE DOCKER

1. Inicializa el servicio de api-piconsulting a través del docker-compose.yml que se brinda en el proyecto.

En cualquiera de los dos casos abre tu navegador web y navega a la dirección `http://localhost:8000/docs`. Esto te llevará a la documentación de la API generada automáticamente por FastAPI.

Puedes encontrar la documentación de FastAPI en el siguiente enlace: https://fastapi.tiangolo.com/
