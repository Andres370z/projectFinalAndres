from request import photos_data
import requests


def consumedatos():
    return print(f"Datos en boyaca.py: {photos_data}")
def consumeApi():
    URL = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(URL)
    if response.status_code == 200:
        print('Solicitud exitosa')
        data = response.json()  # Parsear los datos a JSON
        return data
    else:
        print('Error en la solicitud, detalles:', response.text)