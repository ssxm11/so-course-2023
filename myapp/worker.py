import os
import time
import random
from datetime import datetime

PRIVATE_FOLDER = '/sync_files/private'

def crear_archivo():
    while True:
        numero = random.randint(1000, 9999)
        ahora = datetime.now().strftime("%d%m%Y_%H%M%S")
        nombre_archivo = f"{ahora}.txt"
        ruta_archivo = os.path.join(PRIVATE_FOLDER, nombre_archivo)
        
        with open(ruta_archivo, 'w') as f:
            f.write(str(numero))
        
        print(f"Se creó el archivo: {nombre_archivo} con el número: {numero}")

        # Espera 30 minutos
        time.sleep(10)

if __name__ == "__main__":
    crear_archivo()
