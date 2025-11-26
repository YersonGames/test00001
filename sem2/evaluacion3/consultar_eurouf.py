from usuario_dao import UsuarioDAO
from pwinput import pwinput
import secrets
import hashlib
import base64
import requests
import datetime
import prettytable
from api_deserializar import DeserializarAPI
from registro_dao import RegistroDAO

usuario = UsuarioDAO()
desapi = DeserializarAPI()
registro = RegistroDAO()


#Iniciar sesion
salir = 0
step = 1
while salir == 0:

    while step == 1:
        nombre = input("Nombre de Usuario: ")
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
        datos_usuario = usuario.login_username(nombre)

        if datos_usuario:
            step = 4
        else:
            step = 1

    while step == 4:
        id_usuario = datos_usuario[2]
        iteraciones = int(datos_usuario[3])
        sal = base64.b64decode(datos_usuario[1])
        hash_b = base64.b64decode(datos_usuario[0])

        new_hash_b = hashlib.pbkdf2_hmac("sha256", contrasena.encode("utf-8"), sal, iteraciones  )

        resultado = secrets.compare_digest(hash_b,new_hash_b )
        
        if resultado == True:
            print(f"Haz iniciado sesion como {nombre}")
            step = 0
            salir = 1
        else:
            print("El usuario o contraseña es incorrecta.")
            step = 1

#Menu
salir2 = 0
while salir2 == 0:
    print("""Menu
    1. Consultar indicadore económicos.
    2. Ver historial de Consultas.
    3. Salir""")

    opcion = input("Opcion: ")

    #Consultar
    if opcion == "1":
        date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        url_euro = "https://api.boostr.cl/economy/indicator/euro.json"
        url_uf = "https://api.boostr.cl/economy/indicator/uf.json"

        data_euro = desapi.get_data(url_euro)
        data_uf = desapi.get_data(url_uf)

        if data_euro and data_uf:
            menu = prettytable.PrettyTable()
            menu.field_names = ["Valor euro","Valor UF","Fecha"]
            menu.add_row([data_euro[0],data_uf[0],date])
            print(menu)
            registro.registrar(id_usuario,date,data_euro[0],data_uf[0])

    #Historial
    elif opcion == "2":
        select_r = registro.consultar()
        menu = prettytable.PrettyTable()
        print("\nHistorial Consultas:\n")
        menu.field_names = ["ID","Valor Euro","Valor UF","Usuario","Fecha de Consulta"]
        if select_r:
            for i in select_r:
                menu.add_row([i[0],i[2],i[3],i[1],i[4]])
        print(menu)

    #Salir
    elif opcion == "3":
        salir2 = 1