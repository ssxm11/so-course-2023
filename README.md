# guide 
## pasos seguidos:
1. Modificacion del DockerFile para que se incluyan la carpeta  sync_files y las subcarpetas 
2. bash
``` 
docker build -t synchrontainer .
```
3. incluye endpoints a app.py
4. creamos red
´´´
docker network create sync_net
´´´
5. levantamos 3 contenedores en la red
´´´
docker run -d --name nodo1 --network sync_net synchrontainer
docker run -d --name nodo2 --network sync_net synchrontainer
docker run -d --name nodo3 --network sync_net synchrontainer
´´´
