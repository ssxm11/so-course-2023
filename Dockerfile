# imagen base
FROM python:3
# establece el directorio de trabajo
WORKDIR /usr/src/app
# Copiar la carpeta myapp a /usr/src/app
COPY ./myapp/ .
# instalacion de requerimientos y dependencias
RUN pip3 install --no-cache-dir -r requirements.txt
# Crear las carpetas requeridas por el proyecto
RUN mkdir -p /sync_files/public /sync_files/private
# Aperturo el puerto 5000 del contenedor
EXPOSE 5000
# Establece el entrypoint


COPY ./myapp/start.sh .
RUN chmod +x start.sh
CMD ["./start.sh"]

