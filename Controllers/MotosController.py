
import sys
import os

# Agrega la carpeta raíz al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, jsonify, request
from Utils.Inventario import Inventario
from Models.Moto import Moto

app = Flask(__name__)

@app.route('/api/motos', methods=['GET'])
def obtener_motos():
    motos = Inventario.consultarMotos()
    motos_dict = [moto.to_dict() for moto in motos]
    return jsonify(motos_dict)

@app.route('/api/motos', methods=['POST'])
def guardar_motos():
    data = request.get_json()

    moto = Moto(data=data)
    motos = Inventario.registrarModelo(moto)
    return jsonify({"success" : "ok"})



if __name__ == '__main__':
    app.run(debug=True)
