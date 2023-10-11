# Usamos la imagen oficial de fastapi
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Seteamos el archivo de trtabajo dentro del contenedor
WORKDIR /app

# Copiamos las dependencias del proyecto
COPY requirements.txt .

# Instalamois las depenencias dentro del contenedor
RUN pip install --no-cache-dir -r requirements.txt

# copiamos nuestros archivos dentro de nuestra carpeta en el contenedor
COPY ./app /app

# Exponemos la aplicacion en un puerto que no se encuentre ocupado
EXPOSE 8000

# Luego a travez del shell ejecutamos la aplicacion dentro del contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
