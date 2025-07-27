from flask import Flask, request, jsonify, send_from_directory
import threading
from worker import crear_archivo
import os
app = Flask(__name__)

# Carpeta pública (compartida entre contenedores)
PUBLIC_FOLDER = '/sync_files/public'

# Carpeta privada (solo accesible localmente)
PRIVATE_FOLDER = '/sync_files/private'


# Iniciar hilo para crear archivos
threading.Thread(target=crear_archivo, daemon=True).start()

@app.route('/storage/<uid>')
def storage(uid):
    return os.listdir('/sync_files')

@app.route('/public/')
def public():
    return os.listdir('/sync_files/public')

@app.route('/public/')
def listar_publicos():
    try:
        archivos = os.listdir(PUBLIC_FOLDER)
        return jsonify({"archivos_publicos": archivos})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/storage/<uid>')
def listar_contenedor(uid):
    # Esto solo devuelve los archivos de ESTE contenedor
    try:
        privados = os.listdir(PRIVATE_FOLDER)
        return jsonify({"contenedor": uid, "archivos_privados": privados})
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
    archivo.save(path_destino)
    return jsonify({"mensaje": f"Archivo {filename} subido al contenedor {uid}"}), 200

@app.route('/')
def hello_world():
  return {
    'message': 'hola, Mundo!!!'
  }

@app.route('/despedirse')
def bye_world():
  return {
    'message': 'Adiós, mundo!!!'
  }


app.run()