import requests

url = "https://open.er-api.com/v6/latest/USD"

try:
    respuesta = requests.get(url,timeout=10)
    respuesta.raise_for_status() #lanza error si http es distinto de 200
    data = respuesta.json()

    print(f"1 USD = {data["rates"]["CLP"]} - {data["time_last_update_utc"]}")
    print("Proxima actualizacion: ",data.get("time_next_update_utc"))
except requests.exceptions.HTTPError as error:
    print("Error:",error)