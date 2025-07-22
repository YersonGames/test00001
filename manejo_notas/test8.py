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

def guardar(): #Guardar archivo asignatura/profesores
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

def actualizar_prof(a,b,c,d): #actualizar datos profesores
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
    conexion.updsqldocentes(a,b,c,a2,b2,c2)
    guardar()
    crear_ventana_profesores()

def crear_prof(a,b,c): #Crear nuevo profesor
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
    conexion.addsqldocentes(b,a,c)
    guardar()
    crear_ventana_profesores()

def crear_asig(a,b,c): #Crear nueva asignatura
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
    conexion.addsqlasignaturas(b,a,c)
    guardar()
    crear_ventana_asignaturas()
    
def actualizar_asig(a,b,c,d): #Actualizar datos asignatura
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
    conexion.updsqlasignaturas(a,b,c,a2,b2,c2)
    guardar()
    crear_ventana_asignaturas()
    
def limpiar_ventana(): #Limpiar la ventana
    for widget in ventana.winfo_children():
        widget.destroy()
        
def cargar_db(): #leer y cargar datos des de la base de datos
    global profesores, profesoresrut, profesoresemail, asignaturas, asignaturasab, asignaturasdesc, ventana
    profesores = []
    profesoresrut = []
    profesoresemail = []
    asignaturas = []
    asignaturasab = []
    asignaturasdesc = []
    
    conexion.cursor.execute("select nombre_docente from docentes order by id asc")
    save = conexion.cursor.fetchall()
    for i in range(len(save)):
        profesores.append(save[i][0])
    conexion.cursor.execute("select rut_docente from docentes order by id asc")
    save = conexion.cursor.fetchall()
    for i in range(len(save)):
        profesoresrut.append(save[i][0])
    conexion.cursor.execute("select email_docente from docentes order by id asc")
    save = conexion.cursor.fetchall()
    for i in range(len(save)):
        profesoresemail.append(save[i][0])
    
    conexion.cursor.execute("select nombre_asignatura from asignaturas order by id asc")
    save = conexion.cursor.fetchall()
    for i in range(len(save)):
        asignaturas.append(save[i][0])
    conexion.cursor.execute("select codigo_asignatura from asignaturas order by id asc")
    save = conexion.cursor.fetchall()
    for i in range(len(save)):
        asignaturasab.append(save[i][0])
    conexion.cursor.execute("select descripcion_asignatura from asignaturas order by id asc")
    save = conexion.cursor.fetchall()
    for i in range(len(save)):
        asignaturasdesc.append(save[i][0])
    guardar()
    print("Datos cargados")

def check_login(a): #Verificar si se ha logeado correctamente
    print("check login:",a)
    if a == 1:
        limpiar_ventana()
        crear_ventana2()
        cargar_db()
        #conexion.executesql("insert into docentes(nombre_docente) values('aaaaa');")
    else:
        ventana.after(1000,lambda:check_login(conexion.login))

def crear_ventana1(): #Ventana de login
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

def crear_ventana2(): #ventana de gestion
    global ventana, cursor2check
    cursor2check = 0
    limpiar_ventana()
    tkinter.Label(ventana,text="Gestionar").place(relx=0.5,rely=0,anchor='n')
    btn1 = tkinter.Button(ventana,text="Profesores",command=lambda:crear_ventana_profesores())
    btn1.place(x=400,y=72,anchor='center')
    btn2 = tkinter.Button(ventana,text="Asignaturas",command=lambda:crear_ventana_asignaturas())
    btn2.place(x=400,y=72+(32*1),anchor='center')
    
def crear_ventana_asignaturas(): #ventana de gestion de asignaturas
    global list1, ventana, cursor2check, curname, textsp1a, textsp2a, textsp3a
    cursor2check = 1
    textsp1a = tkinter.StringVar()
    textsp2a = tkinter.StringVar()
    textsp3a = tkinter.StringVar()
    curname = 1
    cargar_db()
    limpiar_ventana()
    tkinter.Label(ventana,text="Asignaturas",padx=0).place(relx=0.5,rely=0,anchor='n')
    list1 = tkinter.Listbox(ventana)
    list1.place(x=400,y=100,anchor='n')
    btn1 = tkinter.Button(ventana,text="Nuevo",command=crear_ventana_crtasig,width=8)
    btn1.place(x=464,y=100,anchor='nw')
    btn2 = tkinter.Button(ventana,text="Modificar",command=crear_ventana_updasig,width=8)
    btn2.place(x=464,y=132,anchor='nw')
    btn3 = tkinter.Button(ventana,text="Eliminar",command=btndelteasignatura,width=8)
    btn3.place(x=464,y=164,anchor='nw')
    btn5 = tkinter.Button(ventana,text="Actualizar",command=btnactasig,width=8)
    btn5.place(x=464,y=192,anchor='nw')
    btn4 = tkinter.Button(ventana,text="Volver",command=crear_ventana2,width=8)
    btn4.place(x=16,y=16,anchor='nw')
    for yy in  range(len(asignaturas)):
        list1.insert(tkinter.END,asignaturas[yy])
    cursorcheck2()

def crear_ventana_profesores(): #ventana de gestion de profesores
    global list1, ventana, cursor2check, curname, textsp1a, textsp2a, textsp3a
    textsp1a = tkinter.StringVar()
    textsp2a = tkinter.StringVar()
    textsp3a = tkinter.StringVar()
    curname = 1
    cursor2check = 1
    cargar_db()
    limpiar_ventana()
    tkinter.Label(ventana,text="Profesores",padx=0).place(relx=0.5,rely=0,anchor='n')
    list1 = tkinter.Listbox(ventana)
    list1.place(x=400,y=100,anchor='n')
    btn1 = tkinter.Button(ventana,text="Nuevo",command=crear_ventana_crtpro,width=8)
    btn1.place(x=464,y=100,anchor='nw')
    btn2 = tkinter.Button(ventana,text="Modificar",command=crear_ventana_updpro,width=8)
    btn2.place(x=464,y=132,anchor='nw')
    btn3 = tkinter.Button(ventana,text="Eliminar",command=btndelteprofesor,width=8)
    btn3.place(x=464,y=164,anchor='nw')
    btn5 = tkinter.Button(ventana,text="Actualizar",command=btnactpro,width=8)
    btn5.place(x=464,y=192,anchor='nw')
    btn4 = tkinter.Button(ventana,text="Volver",command=crear_ventana2,width=8)
    btn4.place(x=16,y=16,anchor='nw')
    for yy in  range(len(profesores)):
        list1.insert(tkinter.END,profesores[yy])
    cursorcheck1()
    
def btnactpro(): #actualizar datos y lista profesores
    global cursor2check
    cursor2check = 0
    cargar_db()
    crear_ventana_profesores()
    
def btnactasig(): #actualizar datos y lista asignaturas
    global cursor2check
    cursor2check = 0
    cargar_db()
    crear_ventana_asignaturas()

def btndelteprofesor(): #boton para eliminar profesores
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
        
def btndelteasignatura(): #boton eliminar asignatura
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
        
def crear_ventana_updpro(): #boton actualizar datos profesor
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
        
        tkinter.Button(ventana,text="Modificar",command=lambda:actualizar_prof(box1.get(),box2.get(),box3.get(),selected)).place(x=400,y=300,anchor='center')
        
def crear_ventana_updasig(): #boton actualizar datos asignatura
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
        
        tkinter.Button(ventana,text="Modificar",command=lambda:actualizar_asig(box1.get(),box2.get(),box3.get(),selected)).place(x=400,y=300,anchor='center')
     

def crear_ventana_crtpro(): #ventana crear nuevo profesor
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

def crear_ventana_crtasig(): #ventana crear nueva asignatura
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

def cursorcheck1(): #verificar seleccion de la lista en profesores
    global ventana, cursor2check, list1, textsp1,textsp2,textsp3,textsel,textsp1a, curname
    indice = -1
    try:
        indice = list1.curselection()
    except tkinter.TclError:
        print("Error al seleccionar cursor, no pasa nada")
    cursor2 = -1
    if indice != -1:
        for i in indice:
            cursor2 = i
        textsel = cursor2
        textsp1a.set("Nombre: "+str(profesores[cursor2]))
        textsp2a.set("RUN: "+str(profesoresrut[cursor2]))
        textsp3a.set("Email: "+str(profesoresemail[cursor2]))
        if cursor2 != -1 and curname == 1:
            textsp1 = tkinter.Label(ventana,textvariable=textsp1a)
            textsp1.place(x=300,y=300,anchor='w')
            textsp2 = tkinter.Label(ventana,textvariable=textsp2a)
            textsp2.place(x=300,y=324,anchor='w')
            textsp3 = tkinter.Label(ventana,textvariable=textsp3a)
            textsp3.place(x=300,y=348,anchor='w')
            curname = 0
            
        if cursor2check == 1:
            ventana.after(100,cursorcheck1)
        print("check list")

def cursorcheck2(): #verificar seleccion de la lista en asignaturas
    global ventana, cursor2check, list1, textsp1,textsp2,textsp3,textsel, textsp1a,textsp2a,textsp3a, curname
    indice = -1
    try:
        indice = list1.curselection()
    except tkinter.TclError:
        print("Error al seleccionar cursor, no pasa nada")
    cursor2 = -1
    if indice != -1:
        for i in indice:
            cursor2 = i
        textsel = cursor2
        textsp1a.set("Nombre: "+str(asignaturas[cursor2]))
        textsp2a.set("Codigo: "+str(asignaturasab[cursor2]))
        textsp3a.set("Descripcion: "+str(asignaturasdesc[cursor2]))
        if cursor2 != -1 and curname == 1:
            textsp1 = tkinter.Label(ventana,textvariable=textsp1a)
            textsp1.place(x=300,y=300,anchor='w')
            textsp2 = tkinter.Label(ventana,textvariable=textsp2a)
            textsp2.place(x=300,y=324,anchor='w')
            textsp3 = tkinter.Label(ventana,textvariable=textsp3a)
            textsp3.place(x=300,y=348,anchor='w')
            curname = 0
        if cursor2check == 1:
            ventana.after(100,cursorcheck2)
        print("check list")  

ventana = tkinter.Tk() #crear la ventana

crear_ventana1()


ventana.mainloop()
exit()
