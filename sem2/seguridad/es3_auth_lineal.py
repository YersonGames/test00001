# es3_aut_lineal
# Registro y Login con PBKDF2-HMAC (sal por usuario) — versión KISS
import sqlite3
import hashlib
import secrets
import base64
from datetime import datetime
from getpass import getpass

# Parámetros simples
DB_PATH = "auth_demo.db"
PBKDF2_ITER = 100_000  # iteraciones recomendadas 

# 1) Conexión y tabla
conn = sqlite3.connect(DB_PATH)
conn.execute("PRAGMA foreign_keys = ON;")
conn.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        salt_b64 TEXT NOT NULL,
        hash_b64 TEXT NOT NULL,
        creado_en TEXT NOT NULL
    );
""")
conn.commit()

# 2) Menú simple
while True:
    print("\n=== Autenticación segura (PBKDF2 + sal) ===")
    print("1) Registrar usuario")
    print("2) Iniciar sesión")
    print("0) Salir")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        # Registro
        username = input("Usuario nuevo: ").strip()
        if not username:
            print("✗ Usuario vacío.")
            continue

        # ¿Existe ya?
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM usuarios WHERE username=?;", (username,))
        if cur.fetchone():
            print("✗ Ya existe ese usuario.")
            continue

        # Lee contraseña en silencio
        password = getpass("Contraseña: ").strip()
        if not password:
            print("✗ Contraseña vacía.")
            continue

        # Genera sal aleatoria de 16 bytes
        salt = secrets.token_bytes(16)

        # Deriva clave con PBKDF2-HMAC-SHA256
        dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, PBKDF2_ITER)

        # Guarda como Base64 (texto) para la BD
        salt_b64 = base64.b64encode(salt).decode()
        hash_b64 = base64.b64encode(dk).decode()

        # Inserta en BD
        conn.execute(
            "INSERT INTO usuarios(username, salt_b64, hash_b64, creado_en) VALUES(?,?,?,?)",
            (username, salt_b64, hash_b64, datetime.now().isoformat())
        )
        conn.commit()
        print("✓ Usuario registrado.")

    elif opcion == "2":
        # Login
        username = input("Usuario: ").strip()
        password = getpass("Contraseña: ").strip()

        cur = conn.cursor()
        cur.execute("SELECT salt_b64, hash_b64 FROM usuarios WHERE username=?;", (username,))
        row = cur.fetchone()
        if not row:
            print("✗ Usuario no existe.")
            continue

        salt_b64, hash_b64 = row

        # Reconstruye binarios desde Base64
        salt = base64.b64decode(salt_b64)
        hash_esperado = base64.b64decode(hash_b64)

        # Recalcula PBKDF2 con la misma sal e iteraciones
        hash_candidato = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, PBKDF2_ITER)

        # Comparación en tiempo constante
        ok = secrets.compare_digest(hash_candidato, hash_esperado)

        if ok:
            print(f"✓ Bienvenido, {username}.")
        else:
            print("✗ Credenciales inválidas.")

    elif opcion == "0":
        print("Chao, compa.")
        break
    else:
        print("Opción no válida.")
