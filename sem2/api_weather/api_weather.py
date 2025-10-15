import requests
from datetime import datetime

url = "https://api.openweathermap.org/data/2.5/weather"

config = {
    "id" : 3868158,
    "appid" : "fe502a036967dfde36cfba56e84a4986",
    "units" : "metric",
    "lang" : "es"
}

try:
    respuesta = requests.request("GET",url,params=config,timeout=10)
    respuesta.raise_for_status()
    data = respuesta.json()

    print(f"{data["name"]}, {data["sys"]["country"]}")
    print(datetime.fromtimestamp(data["dt"]))
    print(data["weather"][0]["description"])
    print(f"Temperatura: {data["main"]["temp"]}°C")

except requests.exceptions.HTTPError as error:
    print("Error:",error)