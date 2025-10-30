import hashlib
import secrets
import base64

from pwinput import pwinput

password = pwinput("Clave: ")
print(password)

#Generar sal aleatoria
sal = secrets.token_bytes(16)
sal_64 = base64.b64encode(sal).decode() #para guadar como texto (Base64)
print(sal_64)

#Derivar el hash (byte) usando el algortimo pkdbf2_hmac

iteraciones = 100_000
hash_b = haslib.pbkf2_hmac("sha256",password.encode("utf-8"),sal,iteraciones)
print(hash_b)
hash_b64 = base64.b64encode(hash_b).decode()
print(hash_b64)
a