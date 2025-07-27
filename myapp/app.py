from flask import Flask, request, jsonify, send_from_directory
import threading
import os
from worker import crear_archivo

app = Flask(__name__)

BASE_PATH = "/sync_files"
PUBLIC_FOLDER = os.path.join(BASE_PATH, "public")
PRIVATE_FOLDER = os.path.join(BASE_PATH, "private")

# Iniciar hilo para crear archivos
threading.Thread(target=crear_archivo, daemon=True).start()

@app.route('/')
def hello():
    return {"message": "Hola, Mundo!!!"}

@app.route('/despedirse')
def bye():
    return {"message": "Adiós, Mundo!!!"}

@app.route('/public/')
def listar_publicos():
    try:
        archivos = os.listdir(PUBLIC_FOLDER)
        return jsonify({"archivos_publicos": archivos})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/storage/<uid>')
def listar_contenedor(uid):
    carpeta_privada = os.path.join(PRIVATE_FOLDER, uid)
    if not os.path.exists(carpeta_privada):
        return jsonify({"error": "Contenedor no encontrado"}), 404
    try:
        archivos = os.listdir(carpeta_privada)
        return jsonify({"contenedor": uid, "archivos_privados": archivos})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download/<filename>')
def download(filename):
    try:
        return send_from_directory(PUBLIC_FOLDER, filename, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@app.route('/upload/<uid>/<filename>', methods=['POST'])
def upload(uid, filename):
    if 'file' not in request.files:
        return jsonify({"error": "No se encontró el archivo en la solicitud"}), 400
    archivo = request.files['file']
    path_destino = os.path.join(PUBLIC_FOLDER, filename)
    try:
        archivo.save(path_destino)
        return jsonify({"mensaje": f"Archivo {filename} subido por el contenedor {uid}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
