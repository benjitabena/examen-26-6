import requests
import json
import os

url = "https://fakestoreapi.com/products"

cantidad_productos = int(input("Ingrese la cantidad de productos que desea obtener: "))
filtracion_de_productos = input("Ingrese que producto desea ver (mens clothing, womens clothing, jewelery, electronics): ")

if not os.path.exists("Descargas"):
    os.makedirs("Descargas")
if not os.path.exists("Imagenes"):
    os.makedirs("Imagenes")

response = requests.get(url)
productos = response.json()

productos_ya_filtrados = [productos for productos in filtracion_de_productos if productos["category"] == filtracion_de_productos]

with open ("Descargas/productos ya filtrados", "w") as file:
    json.dump(productos_ya_filtrados, file)

for producto in productos_ya_filtrados:
    imagen_url = producto["image"]
    imagen_response = requests.get(imagen_url)
    imagen_nombre = os.path.join("Imagenes", f"{producto['id']}.jpg")
    with open(imagen_nombre, "wb") as file:
        file.write(imagen_response.content)

print('Petición descargada')

#queda probar com wifi no ma
