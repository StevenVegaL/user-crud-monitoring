# Usa la imagen oficial de Python como base
FROM python:3.9-slim

# Instalar dependencias necesarias para psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto que FastAPI utilizará
EXPOSE 8000

# Comando para ejecutar FastAPI con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
