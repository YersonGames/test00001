import mysql.connector

def main():
    conexion = mysql.connector.connect(
                host="127.0.0.1",  # en Windows es mejor 127.0.0.1 que 'localhost'
                user="root",
                # password="tu_clave",
                database="crud",
                # Si tu MySQL usa 3307, descomenta la línea siguiente:
                # port=3307,
            )
    cursor = conexion.cursor()

    try:
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        #el ultimo parametros es el que corresponde al parametro OUT del db
        parametros = (nombre,precio,stock,0) #placeholder

        #llamar al procedimiento almacenado
        resultado = cursor.callproc("sp_producto_crear",parametros)

        #el resultado es una lista con corchetes []
        id_nuevo = resultado[-1] #en python el -1 muestra el ultimo dato de la lista
        conexion.commit() #confirmar el grabado de datos
        cursor.close()
        print("Producto creado")
        print("Nuevo id:",id_nuevo)

        cursor = conexion.cursor()

        listar = cursor.callproc("sp_producto_listar_activos")
        
        for result in cursor.stored_results():
            lista = result.fetchall()
            for l in lista:
                print(f"ID: {l[0]} Nombre: {l[1]} Precio: {l[2]} Stock: {l[3]}")
            
    except mysql.connector.Error as error:
        raise ValueError("Error: ",error)

    finally:
        conexion.commit()
        cursor.close()
        conexion.close()

main()