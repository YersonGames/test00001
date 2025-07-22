from data.asignaturas import asignaturas
from data.asignaturas import asignaturasab
from data.asignaturas import asignaturasdesc
from data.profesores import profesores
from data.profesores import profesoresrut
from data.profesores import profesoresemail
#from conexion import cursor
import conexion
import os
import tkinter
import random

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
def actualizar_prof(a,b,c,d):
    a2 = str(profesores[d]).title()
    b2 = profesoresrut[d]
    c2 = profesoresemail[d]
    a = str(a).title().strip()
    b = str(b).strip()
    c = str(c).strip()
    if a == "":
        a = "Sin datos "+str(random.randint(0,10000))
    if b == "":
        b = "Sin datos "+str(random.randint(0,10000))
    if c == "":
        c = "Sin datos "+str(random.randint(0,10000))
    profesores[d] = a.title()
    profesoresrut[d] = b
    profesoresemail[d] = c 
    crear_ventana_profesores()
    conexion.updsqldocentes(a,b,c,a2,b2,c2)
    guardar()

def crear_prof(a,b,c):
    #a = input("Nombre profesor: ").title()
    #b = input("RUT profesor: ")
    #c = input("Email profesor: ")
    a = str(a).title().strip()
    b = str(b).strip()
    c = str(c).strip()
    if a == "":
        a = "Sin datos "+str(random.randint(0,10000))
    if b == "":
        b = "Sin datos "+str(random.randint(0,10000))
    if c == "":
        c = "Sin datos "+str(random.randint(0,10000))
    profesores.append(a)
    profesoresrut.append(b)
    profesoresemail.append(c)
    crear_ventana_profesores()
    conexion.addsqldocentes(b,a,c)
    guardar()
    #conexion.sqldocentes()

def crear_asig(a,b,c):
    #a = input("Nombre profesor: ").title()
    #b = input("RUT profesor: ")
    #c = input("Email profesor: ")
    a = str(a).title().strip()
    b = str(b).strip().upper()
    c = str(c).strip()
    if a == "":
        a = "Sin datos "+str(random.randint(0,10000))
    if b == "":
        b = "Sin datos "+str(random.randint(0,10000))
    if c == "":
        c = "Sin datos "+str(random.randint(0,10000))
    asignaturas.append(a)
    asignaturasab.append(b)
    asignaturasdesc.append(c)
    crear_ventana_asignaturas()
    conexion.addsqlasignaturas(b,a,c)
    guardar()
    #conexion.sqldocentes()
    
def actualizar_asig(a,b,c,d):
    a2 = str(asignaturas[d]).title()
    b2 = asignaturasab[d]
    c2 = asignaturasdesc[d]
    a = str(a).title().strip()
    b = str(b).strip().upper()
    c = str(c).strip()
    if a == "":
        a = "Sin datos "+str(random.randint(0,10000))
    if b == "":
        b = "Sin datos "+str(random.randint(0,10000))
    if c == "":
        c = "Sin datos "+str(random.randint(0,10000))
    asignaturas[d] = a.title()
    asignaturasab[d] = b
    asignaturasdesc[d] = c 
    crear_ventana_asignaturas()
    conexion.updsqlasignaturas(a,b,c,a2,b2,c2)
    guardar()

def execute_sql():
    a = input("Codigo a ejecutar (sql): ")
    conexion.executesql(a)
    

def limpiar_ventana():
    for widget in ventana.winfo_children():
        widget.destroy()
def check_login(a):
    print("check",a)
    if a == 1:
        limpiar_ventana()
        crear_ventana2()
        #conexion.executesql("insert into docentes(nombre_docente) values('aaaaa');")
    else:
        ventana.after(1000,lambda:check_login(conexion.login))

def crear_ventana1():
    ventana.title("Gestion Notas")
    ventana.minsize(800,600)
    ventana.resizable(0,0)

    text1 = tkinter.Label(ventana,text="Iniciar Base de Datos",padx=0).place(relx=0.5,rely=0,anchor='n')
    tkinter.Label(ventana,text='Host').place(x=400,y=72,anchor='center')
    box1 = tkinter.Entry(ventana)
    box1.place(x=400,y=96,anchor='center')
    box1.insert(0,"127.0.0.1")

    tkinter.Label(ventana,text='Port').place(x=400,y=120,anchor='center')
    box2 = tkinter.Entry(ventana)
    box2.place(x=400,y=144,anchor='center')

    tkinter.Label(ventana,text='User').place(x=400,y=168,anchor='center')
    box3 = tkinter.Entry(ventana)
    box3.place(x=400,y=192,anchor='center')

    tkinter.Label(ventana,text='Database').place(x=400,y=216,anchor='center')
    box4 = tkinter.Entry(ventana)
    box4.place(x=400,y=240,anchor='center')

    btn1 = tkinter.Button(ventana,text='Login',command=lambda:conexion.sqlconnect(box1.get(),box2.get(),box3.get(),box4.get()))
    btn1.place(x=400,y=264,anchor='center')

    check_login(conexion.login)

def crear_ventana2():
    global ventana, cursor2check
    cursor2check = 0
    limpiar_ventana()
    tkinter.Label(ventana,text="Gestionar").place(relx=0.5,rely=0,anchor='n')
    btn1 = tkinter.Button(ventana,text="Profesores",command=lambda:crear_ventana_profesores())
    btn1.place(x=400,y=72,anchor='center')
    btn2 = tkinter.Button(ventana,text="Asignaturas",command=lambda:crear_ventana_asignaturas())
    btn2.place(x=400,y=72+(32*1),anchor='center')
    
def crear_ventana_asignaturas():
    global list1, ventana, cursor2check
    cursor2check = 1
    limpiar_ventana()
    tkinter.Label(ventana,text="Asignaturas",padx=0).place(relx=0.5,rely=0,anchor='n')
    list1 = tkinter.Listbox(ventana)
    list1.place(x=400,y=100,anchor='n')
    btn1 = tkinter.Button(ventana,text="Nuevo",command=crear_ventana_crtasig,width=8)
    btn1.place(x=464,y=100,anchor='nw')
    btn2 = tkinter.Button(ventana,text="Actualizar",command=crear_ventana_updasig,width=8)
    btn2.place(x=464,y=132,anchor='nw')
    btn3 = tkinter.Button(ventana,text="Eliminar",command=btndelteasignatura,width=8)
    btn3.place(x=464,y=164,anchor='nw')
    btn4 = tkinter.Button(ventana,text="Volver",command=crear_ventana2,width=8)
    btn4.place(x=16,y=16,anchor='nw')
    for yy in  range(len(asignaturas)):
        list1.insert(tkinter.END,asignaturas[yy])
    cursorcheck2()

def crear_ventana_profesores():
    global list1, ventana, cursor2check
    cursor2check = 1
    limpiar_ventana()
    tkinter.Label(ventana,text="Profesores",padx=0).place(relx=0.5,rely=0,anchor='n')
    list1 = tkinter.Listbox(ventana)
    list1.place(x=400,y=100,anchor='n')
    btn1 = tkinter.Button(ventana,text="Nuevo",command=crear_ventana_crtpro,width=8)
    btn1.place(x=464,y=100,anchor='nw')
    btn2 = tkinter.Button(ventana,text="Actualizar",command=crear_ventana_updpro,width=8)
    btn2.place(x=464,y=132,anchor='nw')
    btn3 = tkinter.Button(ventana,text="Eliminar",command=btndelteprofesor,width=8)
    btn3.place(x=464,y=164,anchor='nw')
    btn4 = tkinter.Button(ventana,text="Volver",command=crear_ventana2,width=8)
    btn4.place(x=16,y=16,anchor='nw')
    for yy in  range(len(profesores)):
        list1.insert(tkinter.END,profesores[yy])
    cursorcheck1()
    
    
def btndelteprofesor():
    global list1, ventana, cursor2check
    indice = list1.curselection()
    for i in indice:
        conexion.delsqldocentes(profesores[i])
        profesores.pop(i)
        profesoresrut.pop(i)
        profesoresemail.pop(i)
        cursor2check = 0
        crear_ventana_profesores()
        guardar()
        
def btndelteasignatura():
    global list1, ventana, cursor2check
    indice = list1.curselection()
    for i in indice:
        conexion.delsqlasignaturas(asignaturas[i])
        asignaturas.pop(i)
        asignaturasab.pop(i)
        asignaturasdesc.pop(i)
        cursor2check = 0
        crear_ventana_asignaturas()
        guardar()
        
def crear_ventana_updpro():
    global ventana,list1
    indice = list1.curselection()
    selected = -1
    for i in indice:
        selected = i
    if selected != -1:
        cursor2check = 0
        limpiar_ventana()
        
        tkinter.Label(ventana,text="Actualizar Profesor").place(relx=0.5,rely=0,anchor='n')
        
        tkinter.Label(ventana,text="Nombre").place(x=400,y=100,anchor='center')
        box1 = tkinter.Entry(ventana)
        box1.place(x=400,y=128,anchor='center')
        box1.insert(0,profesores[selected])
        
        tkinter.Label(ventana,text="Rut").place(x=400,y=128+(28*1),anchor='center')
        box2 = tkinter.Entry(ventana)
        box2.place(x=400,y=128+(28*2),anchor='center')
        box2.insert(0,profesoresrut[selected])
        
        tkinter.Label(ventana,text="Email").place(x=400,y=128+(28*3),anchor='center')
        box3 = tkinter.Entry(ventana)
        box3.place(x=400,y=128+(28*4),anchor='center')
        box3.insert(0,profesoresemail[selected])
        
        tkinter.Button(ventana,text="Actualizar",command=lambda:actualizar_prof(box1.get(),box2.get(),box3.get(),selected)).place(x=400,y=300,anchor='center')
        
def crear_ventana_updasig():
    global ventana,list1
    indice = list1.curselection()
    selected = -1
    for i in indice:
        selected = i
    if selected != -1:
        cursor2check = 0
        limpiar_ventana()
        
        tkinter.Label(ventana,text="Actualizar Asignatura").place(relx=0.5,rely=0,anchor='n')
        
        tkinter.Label(ventana,text="Nombre").place(x=400,y=100,anchor='center')
        box1 = tkinter.Entry(ventana)
        box1.place(x=400,y=128,anchor='center')
        box1.insert(0,asignaturas[selected])
        
        tkinter.Label(ventana,text="Codigo").place(x=400,y=128+(28*1),anchor='center')
        box2 = tkinter.Entry(ventana)
        box2.place(x=400,y=128+(28*2),anchor='center')
        box2.insert(0,asignaturasab[selected])
        
        tkinter.Label(ventana,text="Descripcion").place(x=400,y=128+(28*3),anchor='center')
        box3 = tkinter.Entry(ventana)
        box3.place(x=400,y=128+(28*4),anchor='center')
        box3.insert(0,asignaturasdesc[selected])
        
        tkinter.Button(ventana,text="Actualizar",command=lambda:actualizar_asig(box1.get(),box2.get(),box3.get(),selected)).place(x=400,y=300,anchor='center')
     

def crear_ventana_crtpro():
    global ventana, cursor2check
    cursor2check = 0
    limpiar_ventana()
    tkinter.Label(ventana,text="Nuevo profesor").place(relx=0.5,rely=0,anchor='n')
    
    tkinter.Label(ventana,text="Nombre").place(x=400,y=100,anchor='center')
    box1 = tkinter.Entry(ventana)
    box1.place(x=400,y=128,anchor='center')
    
    tkinter.Label(ventana,text="Rut").place(x=400,y=128+(28*1),anchor='center')
    box2 = tkinter.Entry(ventana)
    box2.place(x=400,y=128+(28*2),anchor='center')
    
    tkinter.Label(ventana,text="Email").place(x=400,y=128+(28*3),anchor='center')
    box3 = tkinter.Entry(ventana)
    box3.place(x=400,y=128+(28*4),anchor='center')
    
    tkinter.Button(ventana,text="Crear",command=lambda:crear_prof(box1.get(),box2.get(),box3.get())).place(x=400,y=300,anchor='center')

def crear_ventana_crtasig():
    global ventana, cursor2check
    cursor2check = 0
    limpiar_ventana()
    tkinter.Label(ventana,text="Nueva asignatura").place(relx=0.5,rely=0,anchor='n')
    
    tkinter.Label(ventana,text="Nombre").place(x=400,y=100,anchor='center')
    box1 = tkinter.Entry(ventana)
    box1.place(x=400,y=128,anchor='center')
    
    tkinter.Label(ventana,text="Codigo").place(x=400,y=128+(28*1),anchor='center')
    box2 = tkinter.Entry(ventana)
    box2.place(x=400,y=128+(28*2),anchor='center')
    
    tkinter.Label(ventana,text="Descripcion").place(x=400,y=128+(28*3),anchor='center')
    box3 = tkinter.Entry(ventana)
    box3.place(x=400,y=128+(28*4),anchor='center')
    
    tkinter.Button(ventana,text="Crear",command=lambda:crear_asig(box1.get(),box2.get(),box3.get())).place(x=400,y=300,anchor='center')

def cursorcheck1():
    global ventana, cursor2check, list1
    indice = -1
    try:
        indice = list1.curselection()
    except tkinter.TclError:
        print("Error al seleccionar cursor, no pasa nada")
    cursor2 = -1
    if indice != -1:
        for i in indice:
            cursor2 = i
        if cursor2 != -1:
            tkinter.Label(ventana,text="Nombre: "+str(profesores[cursor2])).place(x=300,y=300,anchor='w')
            tkinter.Label(ventana,text="RUN: "+str(profesoresrut[cursor2])).place(x=300,y=324,anchor='w')
            tkinter.Label(ventana,text="Email: "+str(profesoresemail[cursor2])).place(x=300,y=348,anchor='w')
        if cursor2check == 1:
            ventana.after(100,cursorcheck1)
        print("check2")
        
def cursorcheck2():
    global ventana, cursor2check, list1
    indice = -1
    try:
        indice = list1.curselection()
    except tkinter.TclError:
        print("Error al seleccionar cursor, no pasa nada")
    cursor2 = -1
    if indice != -1:
        for i in indice:
            cursor2 = i
        if cursor2 != -1:
            tkinter.Label(ventana,text="Nombre: "+str(asignaturas[cursor2])).place(x=300,y=300,anchor='w')
            tkinter.Label(ventana,text="Codigo: "+str(asignaturasab[cursor2])).place(x=300,y=324,anchor='w')
            tkinter.Label(ventana,text="Descripcion: "+str(asignaturasdesc[cursor2])).place(x=300,y=348,anchor='w')
        if cursor2check == 1:
            ventana.after(100,cursorcheck2)
        print("check2")

        

ventana = tkinter.Tk()

crear_ventana1()


ventana.mainloop()
exit()
#a = data.conexion.sqlconnect(x1,x2,x3,x4)
#print(f"Se ha conectado correctamente a la base de datos {x4}")
while False:
    options = ["leer_asignatura","crear_asignatura","buscar_asignatura","actualizar_asignatura","sqldocentes","sqlasignaturas","guardar","help","leer_profesores","buscar_profesores","crear_profesores","eliminar_asignatura","eliminar_profesor","execute_sql","sqladddocentes","sqladdasignaturas","sqlconnect","sqldeldocentes","sqldelasignaturas"]
    b = input("command (help): ").lower().strip()
    if b != "":
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
                    print("Lista de comandos:\n")
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
                    #x5 = input("Password: ")
                    data.conexion.sqlconnect(x1,x2,x3,x4)
                elif options[c] == options[17]:
                    x1 = input("Nombre del docente a eliminar: ")
                    for i in profesores:
                        if x1.lower().strip() in i.lower().strip():
                            print(i)
                            data.conexion.delsqldocentes(i)
                            print(f"El docente {i} ha sido eliminado")
                elif options[c] == options[18]:
                    x1 = input("Nombre de la asignatura a eliminar: ")
                    for i in asignaturas:
                        if x1.lower().strip() in i.lower().strip():
                            print(i)
                            data.conexion.delsqlasignaturas(i)
                            print(f"La asignatura {i} ha sido eliminado")
    if b == "exit":
        break
