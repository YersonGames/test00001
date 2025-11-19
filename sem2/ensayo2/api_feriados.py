import requests

url = "https://api.boostr.cl/holidays.json"

try:
    respuesta = requests.get(url,timeout=10)
    respuesta.raise_for_status() #lanza error si http es distinto de 200
    data = respuesta.json()

    for i in data["data"]:
        print(f"\nFecha: {i["date"]}\nRazon: {i["title"]}\nTipo: {i["type"]}\nInalienable: {i["inalienable"]}\n")
except requests.exceptions.HTTPError as error:
    print("Error:",error)