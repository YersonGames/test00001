import mysql.connector

conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    # port="3307"
    #password="",
    database="iei_170"
)

cursor = conexion.cursor()

#primera consulta
nombre = input("nombre: ")
precio = float(input("precio: "))
stock = int(input("stock: "))
cursor.execute("insert into producto(nombre,precio,stock) values(%s,%s,%s);",(nombre,precio,stock))
conexion.commit()
# filas = cursor.fetchall()
# print("Tablas", filas)

# print("La tabllas son: ")
# for (tabla,) in cursor:
#     print(tabla)

cursor.close()
conexion.close()