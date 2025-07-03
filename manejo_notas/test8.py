from data.asignaturas import asignaturas
from data.asignaturas import asignaturasab
from data.asignaturas import asignaturasdesc
from data.profesores import profesores
from data.profesores import profesoresrut
from data.profesores import profesoresemail
import data.conexion
import os


def leer():
    y = 0
    for x in asignaturas:
        print(x,asignaturasab[y],asignaturasdesc[y])
        y+=1

def buscar():
    a = input("buscar asignatura: ")
    y=0
    for x in asignaturas:
        if a.lower() in x.lower():
            print(x,asignaturasab[y],asignaturasdesc[y])
        y+=1

def crear():
    a = input("Nombre asignatura: ").title()
    b = input("Abreviatura asignatura: ")
    c = input("Descripcion asignatura: ")
    asignaturas.append(a)
    asignaturasab.append(b)
    asignaturasdesc.append(c)

def eliminar():
    a = input("Eliminar asignatura: ")
    y=0
    for x in asignaturas:
        if a.lower() in x.lower():
            asignaturas.remove(x)
            asignaturasab.remove(asignaturasab[y])
            asignaturasdesc.remove(asignaturasdesc[y])
        y+=1

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
    final_file.write(f"asignaturas={asignaturas}\n")
    final_file.write(f"asignaturasab={asignaturasab}\n")
    final_file.write(f"asignaturasdesc={asignaturasdesc}")
    final_file.close()
    file_name = 'profesores.py'
    path1 = os.path.join('manejo_notas/data',file_name)
    path2 = os.path.abspath(path1)
    path3 = os.path.realpath(path2)
    final_file = open(path3,'w+')
    final_file.write(f"profesores={profesores}\n")
    final_file.write(f"profesoresrut={profesoresrut}\n")
    final_file.write(f"profesoresemail={profesoresemail}")
    final_file.close()

def leer_prof():
    a = 0
    for x in profesores:
        print(x,profesoresrut[a],profesoresemail[a])
        a+=1

def buscar_prof():
    a = input("buscar profesor: ")
    b=0
    for x in profesores:
        if a.lower() in x.lower():
            print(x,profesoresrut[b],profesoresemail[b])
        b+=1

def crear_prof():
    a = input("Nombre profesor: ").title()
    b = input("RUT profesor: ")
    c = input("Email profesor: ")
    profesores.append(a)
    profesoresrut.append(b)
    profesoresemail.append(c)

def eliminar_prof():
    a = input("Eliminar profesor: ")
    b = 0
    for x in profesores:
        if a.lower() in x.lower():
            profesores.remove(x)
            profesoresrut.remove(profesoresrut[b])
            profesoresemail.remove(profesoresemail[b])
        b+=1

def execute_sql():
    a = input("Codigo a ejecutar (sql): ")
    data.conexion.executesql(a)
while True:
    options = ["leer_asignatura","crear_asignatura","buscar_asignatura","actualizar_asignatura","sqldocentes","sqlasignaturas","guardar","help","leer_profesores","buscar_profesores","crear_profesores","eliminar_asignatura","eliminar_profesor","execute_sql","sqladddocentes","sqladdasignaturas","sqlconnect"]
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
                data.conexion.sqldocentes()
            elif options[c] == options[5]:
                data.conexion.sqlasignaturas()
            elif options[c] == options[6]:
                guardar()
            elif options[c] == options[7]:
                for x in options:
                    print(x)
            elif options[c] == options[8]:
                leer_prof()
            elif options[c] == options[9]:
                buscar_prof()
            elif options[c] == options[10]:
                crear_prof()
            elif options[c] == options[11]:
                eliminar()
            elif options[c] == options[12]:
                eliminar_prof()
            elif options[c] == options[13]:
                execute_sql()
            elif options[c] == options[14]:
                x = input("Nombre profesor a añadir: ")
                y = 0
                for i in profesores:
                    if x.lower() in i.lower():
                        print(profesoresrut[y],profesores[y],profesoresemail[y],"Ha sido añadido a la base de datos")
                        data.conexion.addsqldocentes(profesoresrut[y],profesores[y],profesoresemail[y])
                    y+=1
            elif options[c] == options[15]:
                x = input("Nombre asignatura a añadir: ")
                y = 0
                for i in asignaturas:
                    if x.lower() in i.lower():
                        print(asignaturasab[y],asignaturas[y],asignaturasdesc[y],"Ha sido añadido a la base de datos")
                        data.conexion.addsqlasignaturas(asignaturasab[y],asignaturas[y],asignaturasdesc[y])
                    y+=1
            elif options[c] == options[16]:
                x1 = input("Host: ")
                x2 = int(input("Port: "))
                x3 = input("User: ")
                x4 = input("Database: ")
                x5 = input("Password: ")
                data.conexion.sqlconnect(x1,x2,x3,x4)
    if b == "exit":
        break
