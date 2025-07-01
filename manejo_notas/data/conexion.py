import mysql.connector;

conexion = mysql.connector.connect(host="127.0.0.1",port=3306,user="root",database="gestion_notas")
cursor = conexion.cursor()

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
#pip3 install mysql-connector