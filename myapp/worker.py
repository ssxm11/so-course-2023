import os
import time
import random
from datetime import datetime
import socket

BASE_FOLDER = '/sync_files/private'

def crear_archivo():
    uid = socket.gethostname()  # usa el nombre del contenedor como uid
    contenedor_folder = os.path.join(BASE_FOLDER, uid)

    # Asegura que exista el directorio privado del contenedor
    os.makedirs(contenedor_folder, exist_ok=True)

    while True:
        numero = random.randint(1000, 9999)
        ahora = datetime.now().strftime("%d%m%Y_%H%M%S")
        nombre_archivo = f"{ahora}.txt"
        ruta_archivo = os.path.join(contenedor_folder, nombre_archivo)

        with open(ruta_archivo, 'w') as f:
            f.write(str(numero))

        print(f"[{uid}] Archivo creado: {nombre_archivo} con número: {numero}")
        time.sleep(1800)  # 30 minutos (1800 segundos)

if __name__ == "__main__":
    crear_archivo()

