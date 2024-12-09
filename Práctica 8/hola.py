import mysql.connector

connection = None  
# Conexión a la base de datos
try:
    connection = mysql.connector.connect(
        host="192.168.1.252",  
        user="PMartinez",            
        password="pokemon", 
        database="Pokemon Battle")

    if connection.is_connected():
        print("Conexión exitosa a la base de datos")

except mysql.connector.Error as error:
    print(f"Error al conectar a la base de datos: {error}")

finally:
    # Verificar si la conexión se creó antes de intentar cerrarla
    if connection and connection.is_connected():
        connection.close()
        print("Conexión cerrada")
    else:
        print("No hay conexión que cerrar")