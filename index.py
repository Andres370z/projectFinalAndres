from flask import Flask, jsonify, render_template
from request import consumeApi, consumeImages
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')


# Ruta para consumir la API
@app.route('/consume_api', methods=['GET'])
def consume_api():
    data = consumeApi()
    print('esta es la data desde index', data)
    if data:
        
        return jsonify(data)
    else:
        return jsonify({"error": "No se pudo obtener datos de la API"}), 500
    
# Ruta para consumir la API
@app.route('/consume_images', methods=['GET'])
def consume_images():
    data = consumeImages()
    print('esta es la data desde index imagenes', data)
    if data:
        
        return jsonify(data)
    else:
        return jsonify({"error": "No se pudo obtener datos de la API"}), 500

    
# reinicia el servidor cada vez que hace un cambio
if __name__== '__main__':
    app.run(debug=True, port=5017)
    
    