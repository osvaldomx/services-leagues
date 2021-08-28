from flask import jsonify

def response(data):
    return jsonify({
        'success': True,
        'data': data
    }), 200

def bad_request(data):
    return jsonify({
        'success': False,
        'data': data,
        'message': "Bad request",
        'code': 400
    }), 400

def unauthorized():
    return jsonify({
        'success': False,
        'data': {},
        'message': "Usuario o contraseña invalidos",
        'code': 401
    }), 401

def not_found():
    return jsonify({
        'success': False,
        'data': {},
        'message': "Recurso no encontrado",
        'code': 404
    }), 404