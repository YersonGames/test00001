import tkinter.messagebox
import mysql.connector;
import tkinter


cursor = 0
conexion = 0
login = 0
def sqlconnect(a,b,c,d):
    global login,cursor,conexion
    a = str(a).strip()
    b = str(b).strip()
    c = str(c).strip()
    d = str(d).strip()
    if a == "":
        a = "null"
    if b == "":
        b = "null"
    if c == "":
        c = "null"
    if d == "":
        d = "null"
    try:
        conexion = mysql.connector.connect(host=a,port=b,user=c,database=d)
        cursor = conexion.cursor()
        print("Conectado a la base de datos")
        login = 1
        return 1
    except mysql.connector.Error:
        tkinter.messagebox.showinfo("Error","Error al conectarse a la base de datos")
        print("Error al conectarse a la base de datos")

def sqldocentes():
    cursor.execute("select * from docentes")
    resultado = cursor.fetchall()
    print(resultado)
    return resultado
def sqlasignaturas():
    cursor.execute("select * from asignaturas")
    resultado = cursor.fetchall()
    print(resultado)
    return resultado

def executesql(a):
    cursor.execute(a)
    resultado = cursor.fetchall()
    print(resultado)
    return resultado

def addsqldocentes(a,b,c):
    global cursor
    cursor.execute(f"insert into gestion_notas.docentes(rut_docente,nombre_docente,email_docente) values('{a}','{b}','{c}');")
    
def addsqlasignaturas(a,b,c):
    cursor.execute(f"insert into asignaturas(codigo_asignatura,nombre_asignatura,descripcion_asignatura) values('{a}','{b}','{c}')")

def delsqldocentes(a):
    cursor.execute(f"delete from docentes where nombre_docente = '{a}'")

def delsqlasignaturas(a):
    cursor.execute(f"delete from asignaturas where nombre_asignatura = '{a}'")
    
def updsqldocentes(a,b,c,a2,b2,c2):
    cursor.execute(f"update docentes set nombre_docente = '{a}' where nombre_docente = '{a2}'")
    cursor.execute(f"update docentes set rut_docente = '{b}' where nombre_docente = '{a}'")
    cursor.execute(f"update docentes set email_docente = '{c}' where nombre_docente = '{a}'")
    
def updsqlasignaturas(a,b,c,a2,b2,c2):
    cursor.execute(f"update asignaturas set nombre_asignatura = '{a}' where nombre_asignatura = '{a2}'")
    cursor.execute(f"update asignaturas set codigo_asignatura = '{b}' where nombre_asignatura = '{a}'")
    cursor.execute(f"update asignaturas set descripcion_asignatura = '{c}' where nombre_asignatura = '{a}'")
#pip3 install mysql-connector