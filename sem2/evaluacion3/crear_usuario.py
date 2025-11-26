from usuario import Usuario
from usuario_dao import UsuarioDAO
from pwinput import pwinput
import secrets
import hashlib
import base64

usuario = UsuarioDAO()

#Pedir datos
salir = 0
step = 1
while salir == 0:
    while step == 1:
        nombre = input("Nombre del usuario: ")
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
        rcontrasena = pwinput("Repita la contraseña: ")
        if contrasena == rcontrasena:
            step = 4
        else:
            print("La contraseña no coincide")
            step = 2

    while step == 4:
        sal = secrets.token_bytes(16)
        sal_64 = base64.b64encode(sal).decode() 

        iteraciones = 100_000
        hash_b = hashlib.pbkdf2_hmac("sha256", contrasena.encode("utf-8"), sal, iteraciones  )
        hash_b64 = base64.b64encode(hash_b).decode()

        nuevo_usuario = Usuario(nombre,hash_b64,sal_64,iteraciones)
        usuario.insertar(nuevo_usuario)
        salir = 1
        step = 0
        print("Usuario creado correctamente")