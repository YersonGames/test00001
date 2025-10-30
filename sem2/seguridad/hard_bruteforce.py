# bruteforce_md5_vs_pbkdf2.py
# Demo KISS: compara fuerza bruta con MD5 vs PBKDF2-HMAC-SHA256.
# Uso educativo en laboratorio. No atacar sistemas reales ni probar contraseñas ajenas.

import hashlib
import itertools
import time
import secrets
import base64
from getpass import getpass
from pwinput import pwinput

print("Demo: Fuerza bruta MD5 vs PBKDF2 (educativo, rápido)")
print("Advertencia: usar solo con contraseñas de ejemplo en el laboratorio.\n")

# 1) Parámetros - puedes cambiarlos antes de ejecutar
conjunto_caracteres = "0123456789"   # espacio de búsqueda: dígitos (explicar por qué)
largo_min = 1
largo_max = 5              # con valores pequeños para que la demo termine rápido en clase
intervalo_impresion = 200  # cada cuántos intentos mostramos progreso

# Parámetros PBKDF2 (ajustar en clase para mostrar distintas velocidades)
iteraciones_pbkdf2 = 20000  # default; baja a 5000 si la máquina es muy lenta

# 2) Contraseña objetivo (la 'víctima' local — no usar reales)
clave_objetivo = pwinput("Escribe la contraseña objetivo (ej: 123): ").strip()
if not clave_objetivo:
    print("Contraseña vacía. Saliendo.")
    raise SystemExit(0)

# 3) Generamos los hashes "almacenados" (simulan lo que un sistema guardaría)
hash_md5_objetivo = hashlib.md5(clave_objetivo.encode("utf-8")).hexdigest()

# PBKDF2 "registro" con salt aleatorio
sal = secrets.token_bytes(16)
sal_b64 = base64.b64encode(sal).decode()
derived = hashlib.pbkdf2_hmac("sha256", clave_objetivo.encode("utf-8"), sal, iteraciones_pbkdf2)
hash_pbkdf2_objetivo = derived.hex()

print("\nHashes objetivo (lo que estaría guardado en un sistema):")
print(" MD5      :", hash_md5_objetivo)
print(" PBKDF2   : (salt base64) ", sal_b64)
print("            (iter)        ", iteraciones_pbkdf2)
print("            (hash hex)    ", hash_pbkdf2_objetivo[:64], "... (truncado)\n")

# 4) Preparar espacio de búsqueda y estimados
estimado_total = sum(len(conjunto_caracteres) ** L for L in range(largo_min, largo_max + 1))
print(f"Espacio de búsqueda aproximado: {estimado_total} intentos (longitudes {largo_min}..{largo_max})")
print("Espacio pequeño a propósito para que la demo termine en clase.\n")

# 5) Ataque con MD5 (rápido)
print("== Ataque MD5 (rápido) ==")
inicio_md5 = time.perf_counter()
intentos_md5 = 0
encontrada_md5 = None

for largo in range(largo_min, largo_max + 1):
    combos_por_largo = len(conjunto_caracteres) ** largo
    intentos_largo = 0
    for producto in itertools.product(conjunto_caracteres, repeat=largo):
        intentos_md5 += 1
        intentos_largo += 1
        intento = "".join(producto)
        hash_intento = hashlib.md5(intento.encode("utf-8")).hexdigest()
        if hash_intento == hash_md5_objetivo:
            tiempo = time.perf_counter() - inicio_md5
            encontrada_md5 = intento
            print(f"\nMD5: ¡Encontrada! '{encontrada_md5}' en {intentos_md5} intentos, {tiempo:.4f} s, {intentos_md5/tiempo:.0f} it/s")
            break
        if intentos_md5 % intervalo_impresion == 0:
            tiempo = time.perf_counter() - inicio_md5
            tasa = intentos_md5 / tiempo if tiempo > 0 else 0
            pct = (intentos_largo / combos_por_largo) * 100
            print(f"\rMD5 intentos: {intentos_md5} | longitud {largo} | {pct:.1f}% de esta longitud | {tasa:.0f} it/s", end="", flush=True)
    if encontrada_md5:
        break

if not encontrada_md5:
    tiempo = time.perf_counter() - inicio_md5
    print(f"\nMD5: No encontrada en espacio probado. intentos={intentos_md5}, tiempo={tiempo:.4f}s")

# 6) Pausa corta antes de PBKDF2 para distinguir en clase
print("\nPresiona Enter para comenzar el ataque PBKDF2 (esto será mucho más lento por intento).")
input()

# 7) Ataque con PBKDF2 (lento por iteraciones)
print("== Ataque PBKDF2-HMAC-SHA256 (usa salt y N iteraciones) ==")
inicio_pbkdf2 = time.perf_counter()
intentos_pbkdf2 = 0
encontrada_pbkdf2 = None

for largo in range(largo_min, largo_max + 1):
    combos_por_largo = len(conjunto_caracteres) ** largo
    intentos_largo = 0
    for producto in itertools.product(conjunto_caracteres, repeat=largo):
        intentos_pbkdf2 += 1
        intentos_largo += 1
        intento = "".join(producto)
        candidato = hashlib.pbkdf2_hmac("sha256", intento.encode("utf-8"), sal, iteraciones_pbkdf2)
        if candidato.hex() == hash_pbkdf2_objetivo:
            tiempo2 = time.perf_counter() - inicio_pbkdf2
            encontrada_pbkdf2 = intento
            print(f"\nPBKDF2: ¡Encontrada! '{encontrada_pbkdf2}' en {intentos_pbkdf2} intentos, {tiempo2:.4f} s, {intentos_pbkdf2/tiempo2:.0f} it/s")
            break
        if intentos_pbkdf2 % intervalo_impresion == 0:
            tiempo2 = time.perf_counter() - inicio_pbkdf2
            tasa2 = intentos_pbkdf2 / tiempo2 if tiempo2 > 0 else 0
            pct = (intentos_largo / combos_por_largo) * 100
            print(f"\rPBKDF2 intentos: {intentos_pbkdf2} | longitud {largo} | {pct:.1f}% de esta longitud | {tasa2:.1f} it/s", end="", flush=True)
    if encontrada_pbkdf2:
        break

if not encontrada_pbkdf2:
    tiempo2 = time.perf_counter() - inicio_pbkdf2
    print(f"\nPBKDF2: No encontrada en el espacio probado. intentos={intentos_pbkdf2}, tiempo={tiempo2:.4f}s")

# 8) Resumen comparativo
print("\n== Resumen comparativo ==")
if encontrada_md5:
    print(f" MD5  -> encontrada: {encontrada_md5} en {intentos_md5} intentos.")
else:
    print(" MD5  -> no encontrada en espacio probado.")
if encontrada_pbkdf2:
    print(f" PBKDF2 -> encontrada: {encontrada_pbkdf2} en {intentos_pbkdf2} intentos.")
else:
    print(" PBKDF2 -> no encontrada en espacio probado.")

print("\nObservación pedagógica:")
print("- MD5 es muy rápido: muchos intentos por segundo (alto it/s).")
print(f"- PBKDF2 con {iteraciones_pbkdf2} iteraciones reduce dramáticamente it/s; cada intento cuesta mucho más.")
print("- Con PBKDF2 + salt + contraseñas robustas, la fuerza bruta práctica se vuelve inviable.\n")

print("Fin demo. Ajusta 'iteraciones_pbkdf2', 'conjunto_caracteres' o 'largo_max' para experimentar otros escenarios.")
