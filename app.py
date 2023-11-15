from flask import Flask, jsonify, request
from markupsafe import escape

app= Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})

@app.route('/usuarios/<string:nombre>')
def usuario_by_name(nombre):
    return jsonify({"name": nombre})

@app.route('/usuarios/<int:id>')
def usuario_by_id(id):
    return jsonify({"id": id})

@app.route('/<path:nombre>')
def no_hacer(nombre):
    return escape(nombre)

# GET todos los 'recursos'
@app.route('/recurso', methods=['GET'])
def get_recursos():
    return jsonify({"data": "lista de los items de este recurso"})

# POST nuevo 'recurso'
@app.route('/recurso', methods=['POST'])
def post_recursos():
    print(request.get_json())
    body= request.get_json()
    name= body()["name"]
    modelo= body()["modelo"]
    #insertar en la BD
    return jsonify({"data": {
        "name": name, 
        "modelo": modelo
}})

# GET un 'recurso' a travez de su id
@app.route('/recurso/<int:id>', methods=['GET'])
def get_recurso_by_id(id):
    #buscar en la base de datos un registro con ese id
    return jsonify({"recurso":{
        "name": "nombre correspondiente a ese id",
        "modelo": "modelo correspondiente a ese id"
    }})



if __name__ == '__main__':
    app.run(debug=True, port=5000)