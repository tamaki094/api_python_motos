import sys
import os



# Agrega la carpeta raíz al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required

# Importacion de Utilerias
from Utils.Inventario import Inventario
from Utils.Accesos import Accesos
from datetime import timedelta

# Importacion de Modelos
from Models.Moto import Moto
from Models.TBModelos import TBModelos

# Configuración de Flask y JWT
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'T0rt4sD3J4m0n_ConQues0YGu4c@Vecindad_2025!'  # Cambiar en producción
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)  # Expira en 1 hora
jwt = JWTManager(app)

# Manejadores de errores JWT
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({
        'error': 'token_expired',
        'msg': 'El token ha expirado'
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'error': 'invalid_token',
        'msg': 'Token inválido'
    }), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'error': 'authorization_required',
        'msg': 'Se requiere token de autorización'
    }), 401

@jwt.needs_fresh_token_loader
def token_not_fresh_callback(jwt_header, jwt_payload):
    return jsonify({
        'error': 'fresh_token_required',
        'msg': 'Se requiere un token fresco'
    }), 401

@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return jsonify({
        'error': 'token_revoked',
        'msg': 'El token ha sido revocado'
    }), 401


# Endpoints de la API

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    print("Data recibida:", data) 
    username = data.get('username')
    password = data.get('password')

    if(Accesos.validate_user(username, password)):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"}), 401

@app.route('/api/conexion', methods=['GET'])
def probar_conexion():
    test = Inventario.probar_conexion()

    if test:
        return jsonify({"success": "ok"})
    return jsonify({"error": "Connection failed"}), 500
    # motos_dict = [moto.to_dict() for moto in motos]
    # return jsonify(motos_dict)

@app.route('/api/modelos', methods=['GET'])
@jwt_required() # Protege esta ruta con JWT
def obtener_modelos():
    try:
        current_user = get_jwt_identity()
        print(f"Usuario autenticado: {current_user}")

        if not current_user:
            return jsonify({"msg": "Usuario no autenticado"}), 401
        modelos = Inventario.consultarModelos()
        return jsonify([modelo.to_dict() for modelo in modelos])
    except Exception as e:
        print("Error al obtener modelos:", e)
        return jsonify({"error": "Error al obtener modelos"}), 500
    
@app.route('/api/modelos/<modelo_id>', methods=['GET'])
@jwt_required()  # Protege esta ruta con JWT
def obtener_modelo_por_id(modelo_id):
    try:
        modelo : TBModelos = Inventario.consultarModeloPorID(modelo_id)
        if modelo:
            return jsonify(modelo.to_dict())
        return jsonify({"error": "Modelo no encontrado"}), 404
    except Exception as e:
        print("Error al obtener el modelo por ID:", e)
        return jsonify({"error": "Error al obtener el modelo por ID"}), 500

@app.route('/api/cilindrajes', methods=['GET'])
def obtener_cilindrajes():
    cilindradas = Inventario.consultarCilindrajes()
    return jsonify([cilindrada.to_dict() for cilindrada in cilindradas])


@app.route('/api/motos', methods=['POST'])
def guardar_motos():
    data = request.get_json()

    moto = Moto(data=data)
    motos = Inventario.registrarModelo(moto)
    return jsonify({"success" : "ok"})



if __name__ == '__main__':
    app.run(debug=True)
