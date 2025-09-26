
import sys
import os

# Agrega la carpeta raíz al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, jsonify, request
from Utils.Inventario import Inventario
from Models.Moto import Moto

app = Flask(__name__)


@app.route('/api/conexion', methods=['GET'])
def probar_conexion():
    test = Inventario.probar_conexion()

    if test:
        return jsonify({"success": "ok"})
    return jsonify({"error": "Connection failed"}), 500
    # motos_dict = [moto.to_dict() for moto in motos]
    # return jsonify(motos_dict)

@app.route('/api/modelos', methods=['GET'])
def obtener_modelos():
    modelos = Inventario.consultarModelos()
    return jsonify([modelo.to_dict() for modelo in modelos])


@app.route('/api/motos', methods=['POST'])
def guardar_motos():
    data = request.get_json()

    moto = Moto(data=data)
    motos = Inventario.registrarModelo(moto)
    return jsonify({"success" : "ok"})



if __name__ == '__main__':
    app.run(debug=True)
