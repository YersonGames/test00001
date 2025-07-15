import mysql.connector;
cursor = 0
conexion = 0
def sqlconnect(a,b,c,d):
    try:
        global cursor,conexion
        conexion = mysql.connector.connect(host=a,port=b,user=c,database=d)
        cursor = conexion.cursor()
        return 1
    except mysql.connector.Error:
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
    cursor.execute(f"insert into docentes(rut_docente,nombre_docente,email_docente) values('{a}','{b}','{c}')")

def addsqlasignaturas(a,b,c):
    cursor.execute(f"insert into asignaturas(codigo_asignatura,nombre_asignatura,descripcion_asignatura) values('{a}','{b}','{c}')")

def delsqldocentes(a):
    cursor.execute(f"delete from docentes where nombre_docente = '{a}'")

def delsqlasignaturas(a):
    cursor.execute(f"delete from asignaturas where nombre_asignatura = '{a}'")
#pip3 install mysql-connector