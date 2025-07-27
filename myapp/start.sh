#!/bin/bash
# Ejecuta worker en segundo plano
python3 worker.py &

# Inicia la app Flask
python3 app.py
