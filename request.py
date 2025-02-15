import requests
import pandas as pd
import json

def consumeApi():
    URL = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(URL)
    if response.status_code == 200:
        print('Solicitud exitosa')
        data = response.json()  # Parsear los datos a JSON
        return data
    else:
        print('Error en la solicitud, detalles:', response.text)
import requests
import pandas as pd
import json

def consumeImages():
    # Clave en mi cuenta
    KEY = 'HLq74gqnrfeoPsUqeKD6zTVuh9KkBfZd3GRuAIn7H4Rs2uPbv9phLbCi'
    URL = 'https://api.pexels.com/v1/search?'
    # Parámetros de búsqueda
    params = {
        'query': 'Boyacá',
        'per_page': 100  # Número de resultados por página
    }
    
    response = requests.get(URL, headers={'Authorization': KEY}, params=params)
    print(response.status_code, response.text)
    # Comprobar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()
        photos = data.get('photos', [])

        # Asegurarse de que hay fotos
        if not photos:
            print("No se encontraron fotos.")
            return json.dumps({"error": "No se encontraron fotos."})

        # Imprimir las URLs de las imágenes y almacenar los datos
        for photo in photos:
            {photo['id']}
            {photo['photographer']}
            {photo['src']['original']}

        # Crear un DataFrame a partir de la lista de fotos
        df = pd.DataFrame(photos)

        # Crear el diccionario de datos finales
        dataFinal = {
            'data': photos,  # Guardar todas las fotos
            'infoMasFotos': None,
            'infoMasFotogra': None
        }

        # Asegurarse de que la columna 'alt' existe antes de procesarla
        if 'alt' in df.columns:
            aportan = df['alt'].value_counts().head(3)
            # print('Lugares con muchas fotos:', aportan)
            dataFinal['infoMasFotos'] = aportan.to_dict()  # Convertir a diccionario para JSON

        if 'photographer' in df.columns:
            aportan = df['photographer'].value_counts().head(1)
            # print('Más fotos por fotógrafo:', aportan)
            dataFinal['infoMasFotogra'] = aportan.to_dict()  # Convertir a diccionario para JSON

        # Convertir dataFinal a JSON
        jsonData = json.dumps(dataFinal)
        return jsonData

    else:
        print(f"Error: {response.status_code}")
        return json.dumps({"error": f"Error en la solicitud: {response.status_code}"})

        



photos_data = consumeImages()

def consumeImagesCundi():
    # Clave en mi cuenta
    KEY = 'HLq74gqnrfeoPsUqeKD6zTVuh9KkBfZd3GRuAIn7H4Rs2uPbv9phLbCi'
    URL = 'https://api.pexels.com/v1/search'
    # Parámetros de búsqueda
    params = {
        'query': 'Boyacá',
        'per_page': 100  # Número de resultados por página
    }

    response = requests.get(URL, headers={'Authorization': KEY}, params=params)

    # Comprobar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()
        photos = data.get('photos', [])

        # Asegurarse de que hay fotos
        if not photos:
            print("No se encontraron fotos.")
            return json.dumps({"error": "No se encontraron fotos."})

        # Imprimir las URLs de las imágenes y almacenar los datos
        for photo in photos:
            {photo['id']}
            {photo['photographer']}
            {photo['src']['original']}

        # Crear un DataFrame a partir de la lista de fotos
        df = pd.DataFrame(photos)

        # Crear el diccionario de datos finales
        dataFinal = {
            'data': photos,  # Guardar todas las fotos
            'infoMasFotos': None,
            'infoMasFotogra': None
        }

        # Asegurarse de que la columna 'alt' existe antes de procesarla
        if 'alt' in df.columns:
            aportan = df['alt'].value_counts().head(3)
            # print('Lugares con muchas fotos:', aportan)
            dataFinal['infoMasFotos'] = aportan.to_dict()  # Convertir a diccionario para JSON

        if 'photographer' in df.columns:
            aportan = df['photographer'].value_counts().head(1)
            # print('Más fotos por fotógrafo:', aportan)
            dataFinal['infoMasFotogra'] = aportan.to_dict()  # Convertir a diccionario para JSON

        # Convertir dataFinal a JSON
        jsonData = json.dumps(dataFinal)
        return jsonData

    else:
        print(f"Error: {response.status_code}")
        return json.dumps({"error": f"Error en la solicitud: {response.status_code}"})

        
photos_dataCundi = consumeImagesCundi()




def consumeImagesCundi2(paramsSerch):
    
    headers = {
    'x-freepik-api-key': 'FPSX2941515ef8534d28843962375cbeb2d1'
    }
    params = {
        'term': paramsSerch,  # El término de búsqueda
        'limit': '100'
    }
    response = requests.get('https://api.freepik.com/v1/resources', headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        # Obtener las fotos de la respuesta
        photos = data.get('data', [])

        # Asegurarse de que hay fotos
        if not photos:
            print("No se encontraron fotos.")
            return json.dumps({"error": "No se encontraron fotos."})

        # Imprimir las URLs de las imágenes, el título y el fotógrafo
        for photo in photos:
            photo['id']
            photo['title']
            photo['author']['name']
            photo['image']['source']['url']

        # Crear un DataFrame a partir de las fotos
        df = pd.DataFrame(photos)

        # Crear el diccionario de datos finales
        dataFinal = {
            'data': photos,  # Guardar todas las fotos
            'infoMasFotos': None,
            'infoMasFotogra': None
        }

        # Verificar si 'title' existe en las columnas antes de procesarlo
        if 'title' in df.columns:
            aportan = df['title'].value_counts().head(3)
            dataFinal['infoMasFotos'] = aportan.to_dict()  # Convertir a diccionario para JSON

        # Verificar si 'author' existe en las columnas antes de procesarlo
        if 'author' in df.columns:
            aportan = df['author'].apply(lambda x: x['name']).value_counts().head(1)
            dataFinal['infoMasFotogra'] = aportan.to_dict()  # Convertir a diccionario para JSON

        # Convertir dataFinal a JSON
        jsonData = json.dumps(dataFinal, indent=4)
        return jsonData

    else:
        print(f"Error: {response.status_code}")
        return json.dumps({"error": f"Error en la solicitud: {response.status_code}"})


# Llamada a la función con el término de búsqueda

        
# Comprobar si hay datos y crear el DataFrame


