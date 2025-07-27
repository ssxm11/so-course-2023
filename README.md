# Synchrontainer

Proyecto final de Sistemas Operativos
---

## Objetivo

Desarrollar una red de contenedores Docker capaz de:

- Crear archivos de manera periódica.
- Compartir archivos públicos entre contenedores.
- Gestionar archivos privados por contenedor.
- Exponer endpoints REST para consultar, subir y descargar archivos.

---

## Guía 

### Estructura del proyecto
### Estructura del proyecto

```bash
/so-course-2023/
├── myapp/
│   ├── app.py
│   ├── requirements.txt
│   ├── worker.py
│   └── start.sh
├── Dockerfile
├── docker-compose.yml
└── README.md
```


---


### 1. Modificación del `Dockerfile`

- Se agregaron las carpetas `sync_files/public` y `sync_files/private`.

### 2. Compilación de la imagen Docker

```bash
docker build -t synchrontainer .
```

### 3.  Inclusión de endpoints en app.py

/public/ — Lista archivos públicos.

/storage/<uid> — Lista archivos privados del contenedor.

/download/<filename> — Descarga un archivo público.

/upload/<uid>/<filename> — Sube un archivo a la red pública.

### 4. Uso de `start.sh`

La creacion de este hace que el contenedor arranque automáticamente ejecutando `start.sh`, el cual:
- Asegura que se creen las carpetas `/sync_files/public` y `/sync_files/private/<uid>`
- Inicia el generador automático de archivos (`worker.py`)
- Inicia el servidor Flask (`app.py`)

### 5. Creación de una red Docker personalizada
```bash
docker network create sync_net
```
### 6. Levantamiento de 3 contenedores manualmente (modo prueba)
```bash
docker run -d --name nodo1 --network sync_net -p 5001:5000 synchrontainer
docker run -d --name nodo2 --network sync_net -p 5002:5000 synchrontainer
docker run -d --name nodo3 --network sync_net -p 5003:5000 synchrontainer
```

### 7. creacion del docker-compose para crear lo contenedores automaticamente

### 8. para ejecutar
```bash
docker-compose up --build
```

### para apagar todo
```bash
docker-compose down -v
```

#### autor

Estudiante: Esteban Samuel Cordoba Narvaez
codigo: 202370976 - 3743
correo: esteban.cordoba@correounivalle.edu.co
github user: ssxm11

---