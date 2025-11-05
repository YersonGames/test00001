from usuario import Usuario
from usuario_dao import UsuarioDAO
from pwinput import pwinput
import secrets
import hashlib
import base64
import requests
import datetime

#Iniciar Sesion
usuario = UsuarioDAO()

salir = 1
while salir == 1:
    step = 1
    while step == 1:
        nombre = input("Nombre: ")

        if not nombre:
            print("Error: El campo esta vacio")
        else:
            step = 2

    while step == 2:
        contrasena = pwinput("Contraseña: ")

        if not contrasena:
            print("Error: El campo esta vacio")
        else:
            step = 3

    while step == 3:
        select = usuario.login_username(nombre)

        if select:
            step = 4
        else:
            step = 1

    while step == 4:
        sal = base64.b64decode(select[1])
        hash_b = base64.b64decode(select[0])

        iteraciones = 100_000
        new_hash_b = hashlib.pbkdf2_hmac("sha256", contrasena.encode("utf-8"), sal, iteraciones  )

        resultado = secrets.compare_digest(hash_b,new_hash_b )
        
        if resultado == True:
            print(f"Haz iniciado sesion como {nombre}")
            step = 0
            salir = 0
        else:
            print("El usuario o contraseña es incorrecta.")
            step = 1

#Menu
salir2 = 1
while salir2 == 1:
    print("""Menu
    1. Consultar Dolar.
    2. Ver historial de Consultas.
    3. Salir""")
    
    opcion = input("Opcion: ")

    if opcion == "1":
        date = datetime.datetime.today()
        url = f"https://findic.cl/api/dolar/{date.day}-{date.month}-{date.year}"

        try:
            respuesta = requests.get(url,timeout=10)
            respuesta.raise_for_status() 
            data = respuesta.json()
            
            print(f"\nUSD: {data["serie"]["valor"]}\nFecha: {data["serie"]["fecha"]}\n")

        except requests.exceptions.HTTPError as error:
            print("Error:",error)
    elif opcion == "3":
        salir2 = 0
