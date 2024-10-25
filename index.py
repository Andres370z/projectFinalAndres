from flask import Flask, jsonify, render_template, redirect, url_for
from request import consumeApi, consumeImages, consumeImagesCundi, consumeImagesCundi2
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('index.html')



@app.route('/cundinamarca')
def cundinamarca():
    return render_template('cundinamarca.html')

@app.route('/boyaca')
def boyaca():
    return render_template('boyaca.html')

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

# Ruta para consumir la API
@app.route('/consume_images', methods=['GET'])
def consume_images():
    data = consumeImages()
    print('esta es la data desde index imagenes', data)
    if data:
        
        return jsonify(data)
    else:
        return jsonify({"error": "No se pudo obtener datos de la API"}), 500
    


@app.route('/consume_images_cundinamarca', methods=['GET'])
def consume_images_Cundinamarcar():
    data = consumeImagesCundi()
    print('esta es la data desde index imagenes', data)
    if data:
        
        return jsonify(data)
    else:
        return jsonify({"error": "No se pudo obtener datos de la API"}), 500


@app.route('/consume_images_cundinamarca2', methods=['GET'])
def consume_images_cundinamarca2():
    data = consumeImagesCundi2('Boyaca')
    print('esta es la data desde index imagenes', data)
    if data:
        
        return jsonify(data)
    else:
        return jsonify({"error": "No se pudo obtener datos de la API"}), 500
@app.route('/consume_images_Boyaca2', methods=['GET'])
def consume_images_Boyaca2():
    data = consumeImagesCundi2('Cundinamarca biodiversidad')
    print('esta es la data desde index imagenes', data)
    if data:
        
        return jsonify(data)
    else:
        return jsonify({"error": "No se pudo obtener datos de la API"}), 500


# reinicia el servidor cada vez que hace un cambio
if __name__== '__main__':
    app.run(debug=True, port=5017)
    
    
    
    