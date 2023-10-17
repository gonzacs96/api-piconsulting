FROM python:3.10.11-slim-buster AS build

# Evitar que Python genere archivos bytecode .pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Evitar que Python guarde en la memoria caché las dependencias instaladas
ENV PYTHONUNBUFFERED 1

# Instalar las dependencias necesarias para compilar algunos paquetes de Python
RUN apt-get update

# Copiar el código de la aplicación al directorio /app dentro del contenedor
COPY . /app

# Establecer /app como el directorio de trabajo actual
WORKDIR /app

# Crear y activar el entorno virtual
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Etapa de ejecución	
FROM python:3.10.11-slim-buster AS runtime

# Copiar el código de la aplicación y el entorno virtual desde la etapa de compilación
COPY --from=build /opt/venv /opt/venv
COPY --from=build /app /app

# Establecer /app como el directorio de trabajo actual
WORKDIR /app

# Activar el entorno virtual
ENV PATH="/opt/venv/bin:$PATH"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
