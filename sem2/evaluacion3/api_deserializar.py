import requests
class DeserializarAPI:
    def __init__(self):
        pass

    def get_data(self,url):
        try:
            respuesta = requests.get(url,timeout=10)
            respuesta.raise_for_status() 
            data = respuesta.json()


            api1_data = data["data"]["value"]
            api1_data2 = data["data"]["date"]

            return [api1_data,api1_data2]
        
        except requests.exceptions.HTTPError as error:
            print("Error:",error)
        except requests.JSONDecodeError as error:
            print("Error:",error)
        except requests.Timeout as error:
            print("Error:",error)
        except requests.ConnectionError as error:
            print("Error:",error)
        except requests.ConnectTimeout as error:
            print("Error:",error)
        except requests.RequestException as error:
            print("Error:",error)