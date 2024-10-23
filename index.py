from flask import Flask, jsonify, render_template
from request import consumeApi, consumeImages
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/descubre')
def descubre():
    return render_template('descubre.html')

@app.route('/boyaca')
def boyaca():
    return render_template('boyaca.html')


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
    
    
    
    