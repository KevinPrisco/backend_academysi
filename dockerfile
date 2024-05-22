FROM python:3.11.9

# Establece el directorio de trabajo
WORKDIR /code

# Copia el archivo requirements.txt en el directorio de trabajo
COPY ./requirements.txt /code/requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copia el contenido del directorio src en el directorio de trabajo
COPY ./src /code/src

# Establece el comando por defecto para ejecutar la aplicación
CMD ["uvicorn", "src.main:app", "--host", "127.0.0.0", "--port", "8000"]