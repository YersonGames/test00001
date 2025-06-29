from data.asignaturas import asignaturas
import data.conexion
import os


def leer():
    for x in asignaturas:
        print(x)

def buscar():
    a = input("buscar asignatura: ")
    for x in asignaturas:
        if a.lower() in x.lower():
            print(x)

def crear():
    a = input("Crear asignatura: ").title()
    asignaturas.append(a)

def actualizar():
    search = 0
    a = input("Asignatura a actualizar [asignatura] [nuevo nombre]: ").split(" ")
    if len(a) == 2:
        for num in range(len(asignaturas)):
            if a[0].lower() in asignaturas[num].lower():
                print(f"Se actualizo la asignatura {asignaturas[num]} a {a[1]}")
                asignaturas[num] = a[1].title()
                search = 1
                break
        if search == 0:
            print("Error: No se encontro la asignatura para actualizar")
    else:
        print("Error: Escribe 2 nombres separado por 1 espacio")

def guardar():
    file_name = 'asignaturas.py'
    path1 = os.path.join('manejo_notas/data',file_name)
    path2 = os.path.abspath(path1)
    path3 = os.path.realpath(path2)
    final_file = open(path3,'w+')
    final_file.write(f"asignaturas={asignaturas}")
    final_file.close()

while True:
    options = ["leer","crear","buscar","actualizar","sqldocentes","guardar","help"]
    b = input("command: ").lower().strip()

    for c in range(len(options)):
        if b.lower() in options[c]:
            if options[c] == options[0]:
                leer()
            elif options[c] == options[1]:
                crear()
            elif options[c] == options[2]:
                buscar()
            elif options[c] == options[3]:
                actualizar()
            elif options[c] == options[4]:
                guardar()
            elif options[c] == options[5]:
                data.conexion.sqldocentes()
            elif options[c] == options[6]:
                for x in options:
                    print(x)
    if b == "exit":
        break
