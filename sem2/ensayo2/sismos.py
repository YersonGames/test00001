# ================================================================
# CUADERNO DE PRÁCTICA: AUTENTICACIÓN, API DE SISMOS Y SQLITE
# ================================================================
# Cada sección contiene explicaciones ANTES del código
# ================================================================



# ================================================================
# SECCIÓN 1: IMPORTACIÓN DE LIBRERÍAS + CREACIÓN DE BASE LOCAL
# ================================================================
# Aquí preparamos lo básico que toda app necesita:
# - sqlite3 para almacenar usuarios y registros
# - hashlib para proteger contraseñas
# - requests para consultar APIs reales
# - datetime para registrar fecha/hora de consultas
# ================================================================

import sqlite3
import hashlib
import requests
from datetime import datetime

print("\n=== SECCIÓN 1: INICIALIZANDO BASE DE DATOS ===")

# Conexión inicial y creación de tablas
conn = sqlite3.connect("sismos.db") #creamos la variable de conexion a bd
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    usuario TEXT PRIMARY KEY,
    hash TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS registros_sismo(
    fecha TEXT,
    hora TEXT,
    lugar TEXT,
    magnitud TEXT,
    consultado_en TEXT
)
""")

conn.commit() # grabamos los cambios
conn.close() # cerramo conexion a bd

print("Base de datos creada/lista.\n")



# ================================================================
# SECCIÓN 2: FUNCIONES DE AUTENTICACIÓN CON HASH (SHA-256)
# ================================================================
# Aquí se crea un usuario y se valida.
# SHA-256 convierte la contraseña en un hash irreversible.
# Esto es lo mismo que necesitarás dominar para la ES3.
# ================================================================

print("=== SECCIÓN 2: AUTENTICACIÓN ===")

def crear_usuario(usuario, password):
    """
    Crea usuario en SQLite y almacena hash SHA-256.
    """
    conn = sqlite3.connect('sismos.db') #conectanos bd
    cursor = conn.cursor()

    hash_pass = hashlib.sha256(password.encode()).hexdigest()

    try:
        cursor.execute(
            "INSERT INTO usuarios(usuario, hash) VALUES (?, ?)",
            (usuario, hash_pass)
        )
        conn.commit()
        print(f"Usuario '{usuario}' creado correctamente.")
    except sqlite3.IntegrityError:
        print("El usuario ya existe.")
    finally:
        conn.close()


def login(usuario, password):
    """
    Valida usuario y contraseña usando hash.
    """
    conn = sqlite3.connect('sismos.db')
    cursor = conn.cursor()

    cursor.execute("SELECT hash FROM usuarios WHERE usuario=?", (usuario,))
    fila = cursor.fetchone()
    conn.close()

    if fila is None:
        print("Usuario no encontrado.")
        return False

    hash_pass = hashlib.sha256(password.encode()).hexdigest()

    if hash_pass == fila[0]:
        print("Login correcto.")
        return True
    else:
        print("Contraseña incorrecta.")
        return False


print("Funciones de autenticación listas.\n")



# ================================================================
# SECCIÓN 3: CONSUMO DE API DE SISMOS
# ================================================================
# Aquí consultamos la API real:
# https://api.boostr.cl/earthquake.json
#
# Explicamos:
# - requests.get()
# - manejo de excepciones con try/except
# - cómo deserializar JSON en Python
# ================================================================

print("=== SECCIÓN 3: CONSUMO DE API ===")

def consultar_sismo():
    url = "https://api.boostr.cl/earthquake.json"

    try:
        r = requests.get(url, timeout=5) #hacemos la consulta
        r.raise_for_status()

        data = r.json() # sepaamos el JSON de respuesta
        s = data["data"] # sección principal del JSON de respuesta

        # aquí cada s["xxxx"] es un "key" dentro de la seccion "data" del JSON de respuesta
        print("\n=== ÚLTIMO SISMO REPORTADO ===")
        print("Fecha:", s["date"])  
        print("Hora :", s["hour"])
        print("Lugar:", s["place"])
        print("Magnitud:", s["magnitude"])

        return s

    except Exception as e:
        print("Error al consultar API:", e)
        return None

print("Función de API lista.\n")

# ================================================================
# SECCIÓN 4: REGISTRO LOCAL EN SQLITE3
# ================================================================
# Guardamos el sismo consultado junto al momento en que se pidió.
# Esto simula exactamente lo que harán con la ES3
# (pero allá será UF, IPC, UTM, etc.)
# ================================================================

print("=== SECCIÓN 4: REGISTRO LOCAL ===")

def registrar_sismo(s):
    if s is None:
        print("Nada que registrar (sismo = None).")
        return

    conn = sqlite3.connect('sismos.db')
    cursor = conn.cursor()

    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO registros_sismo(fecha, hora, lugar, magnitud, consultado_en)
        VALUES (?, ?, ?, ?, ?)
    """, (s["date"], s["hour"], s["place"], s["magnitude"], ahora))

    conn.commit()
    conn.close()

    print("Registro almacenado correctamente.\n")



# ================================================================
# SECCIÓN 5: VER HISTORIAL DE CONSULTAS
# ================================================================
# Simplemente listamos todos los valores guardados en la tabla de 
# registros_sismo
# ================================================================

print("=== SECCIÓN 5: HISTORIAL ===")

def ver_historial():
    conn = sqlite3.connect('sismos.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM registros_sismo")
    filas = cursor.fetchall()
    conn.close()

    print("\n=== HISTORIAL DE CONSULTAS ALMACENADAS ===")
    for f in filas:
        print(f)
    print()



# ================================================================
# SECCIÓN 6: MINI MENÚ DE PRUEBA
# ================================================================
# Esto combina todo:
# - login
# - consumo API
# - registro local
# - historial
# ================================================================

print("=== SECCIÓN 6: MENÚ ===")

def menu():
    usu = input("Usuario: ")
    pwd = input("Contraseña: ")

    if not login(usu, pwd):
        return
    salir = False
    while not salir:
        print("\nMENU PRINCIPAL")
        print("1. Consultar sismo")
        print("2. Ver historial")
        print("3. Salir")

        op = input("Opción: ")

        if op == "1":
            s = consultar_sismo()
            registrar_sismo(s)
        elif op == "2":
            ver_historial()
        elif op == "3":
            print("Saliendo del sistema...")
            salir = True
        else:
            print("Opción no valida.")

# ================================================================
# SECCIÓN FINAL: SUGERENCIA PARA PRUEBAS
# ================================================================
# Descomenta la línea que necesites para ir probando cada parte.
# Esto permite pueda ejecutar en el mismo programa los 2 comportamientos,
# ================================================================

# crear_usuario("admin", "1234")
# menu()
