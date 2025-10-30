# Demo KISS de fuerza bruta (educativo) con indicador de progreso.
# Usa MD5 para que sea rápido. No atacar sistemas reales ni probar contraseñas ajenas.

import hashlib
import itertools
import time
from getpass import getpass

print("=== Demo: Fuerza bruta simple con progreso (educativo) ===")
print("Advertencia: usar solo con contraseñas de ejemplo en el laboratorio.")
print()

# contraseña objetivo (el 'atacante' solo tendría el hash)
clave_objetivo = getpass("Escribe la contraseña objetivo (ej: 1234) para que el script la 'tenga' localmente: ").strip()
if not clave_objetivo:
    print("Nada para probar. Saliendo.")
    raise SystemExit(0)

hash_objetivo = hashlib.md5(clave_objetivo.encode("utf-8")).hexdigest()
print("\nHash objetivo (MD5 hex):", hash_objetivo)
print("Ahora el script intentará adivinar la contraseña por fuerza bruta (combinaciones cortas).")
print()

# parámetros (ajustables, KISS)
conjunto_caracteres = "0123456789"   # caracteres probados
largo_min = 1
largo_max = 6              # con 10^6 = 1000000 pruebas en total (rápido)
intervalo_impresion = 500  # cada cuántos intentos mostramos progreso

# cálculo rápido del total aproximado (solo para info)
estimado_total = sum(len(conjunto_caracteres) ** L for L in range(largo_min, largo_max + 1))
print(f"Espacio de búsqueda aproximado: {estimado_total} intentos totales (longitudes {largo_min}..{largo_max})")
print(f"Mostraremos progreso cada {intervalo_impresion} intentos.\n")

inicio_tiempo = time.perf_counter()
intentos_totales = 0
encontrado = None

try:
    for largo in range(largo_min, largo_max + 1):
        combos_por_largo = len(conjunto_caracteres) ** largo
        intentos_largo = 0

        for producto in itertools.product(conjunto_caracteres, repeat=largo):
            intentos_totales += 1
            intentos_largo += 1

            intento = "".join(producto)
            hash_intento = hashlib.md5(intento.encode("utf-8")).hexdigest()

            if hash_intento == hash_objetivo:
                tiempo_transcurrido = time.perf_counter() - inicio_tiempo
                print()
                print("¡Contraseña encontrada!")
                print("  contraseña :", intento)
                print("  intentos    :", intentos_totales)
                print(f"  tiempo      : {tiempo_transcurrido:.4f} s")
                print(f"  velocidad   : {intentos_totales/tiempo_transcurrido:.0f} intentos/s")
                encontrado = intento
                break

            # Mostrar progreso periódico
            if intentos_totales % intervalo_impresion == 0:
                tiempo_transcurrido = time.perf_counter() - inicio_tiempo
                velocidad = intentos_totales / tiempo_transcurrido if tiempo_transcurrido > 0 else 0
                pct_largo = (intentos_largo / combos_por_largo) * 100
                # imprimimos en la misma línea para no llenar la consola
                print(f"\rIntentos: {intentos_totales} | longitud actual: {largo} | "
                      f"progreso longitud: {pct_largo:.1f}% | velocidad: {velocidad:.0f} it/s | intento: {intento}",
                      end="", flush=True)

        if encontrado:
            break

except KeyboardInterrupt:
    print("\nInterrumpido por el usuario (Ctrl+C).")

if not encontrado:
    tiempo_transcurrido = time.perf_counter() - inicio_tiempo
    print()
    print("No se encontró la contraseña en el espacio probado.")
    print("  intentos   :", intentos_totales)
    print(f"  tiempo     : {tiempo_transcurrido:.4f} s")
    print(f"  velocidad  : {intentos_totales/tiempo_transcurrido:.0f} intentos/s" if tiempo_transcurrido > 0 else "  velocidad  : 0 it/s")

print()
print("---- Observación pedagógica ----")
print("Demo usa MD5 (rápido). Si en vez de MD5 el sistema usa PBKDF2 con 100.000 iteraciones,")
print("cada intento sería mucho más lento y la velocidad (it/s) caería dramáticamente.")
