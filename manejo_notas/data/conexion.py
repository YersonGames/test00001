import mysql.connector;
conexion = mysql.connector.connect(host="127.0.0.1",port=3306,user="root",database="gestion_notas")
cursor = conexion.cursor()

def sqldocentes():
    cursor.execute("select * from docentes")
    resultado = cursor.fetchall()
    print(resultado)
    return resultado
#pip3 install mysql-connector