from usuario import Usuario
from usuario_dao import UsuarioDAO
from pwinput import pwinput
import secrets
import hashlib
import base64

usuario = UsuarioDAO()

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
        step = 0

sal = secrets.token_bytes(16)
sal_64 = base64.b64encode(sal).decode() 

iteraciones = 100_000
hash_b = hashlib.pbkdf2_hmac("sha256", contrasena.encode("utf-8"), sal, iteraciones  )
hash_b64 = base64.b64encode(hash_b).decode()


nuevo_usuario = Usuario(nombre,hash_b64,sal_64)
usuario.insertar(nuevo_usuario)

print("Usuario Creado!!!")