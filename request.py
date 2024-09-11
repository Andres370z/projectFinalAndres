import requests

def consumeApi():
    URL = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(URL)
    if response.status_code == 200:
        print('Solicitud exitosa')
        data = response.json()  # Parsear los datos a JSON
        return data
    else:
        print('Error en la solicitud, detalles:', response.text)
    
def consumeImages():
    # clave en mi cuenta
    KEY = 'HLq74gqnrfeoPsUqeKD6zTVuh9KkBfZd3GRuAIn7H4Rs2uPbv9phLbCi'
    URL = 'https://api.pexels.com/v1/search'
    # Parámetros de búsqueda
    params = {
        'query': 'Boyacá',
        'per_page': 10  # Número de resultados por página
    }
    response = requests.get(URL, headers={'Authorization': KEY}, params=params)
    # Comprobar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()
        photos = data.get('photos', [])
    
    # Imprimir las URLs de las imágenes
        for photo in photos:
            print(f"ID: {photo['id']}")
            print(f"Photographer: {photo['photographer']}")
            print(f"URL: {photo['src']['original']}\n")
        return photos
    else:
        print(f"Error: {response.status_code}")