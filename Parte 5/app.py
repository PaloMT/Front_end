import streamlit as st
import mysql.connector
import pandas as pd

# Configuración de conexión a MySQL
def conectar_db():
    return mysql.connector.connect(
        host="192.168.1.252",  
        user="PMartinez",            
        password="", 
        database="Pokemon Battle")


def obtener_ataques():
    conexion = conectar_db()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ataques_pokemon;")
    resultados = cursor.fetchall()
    conexion.close()
    return pd.DataFrame(resultados)

# Función para agregar un nuevo ataque
def agregar_ataque(nombre, tipo, potencia, precision):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO ataques_pokemon (nombre, tipo, potencia, precision) VALUES (%s, %s, %s, %s)", 
        (nombre, tipo, potencia, precision)
    )
    conexion.commit()
    conexion.close()

# Interfaz en Streamlit
st.title("Gestión de Ataques Pokémon")

 #Botón para mostrar la tabla completa
if st.button("Ver tabla completa"):
    ataques = obtener_ataques()
    if not ataques.empty:
        st.write("Tabla de ataques Pokémon:")
        st.dataframe(ataques)
    else:
        st.warning("La tabla de ataques está vacía.")

# Mostrar tabla de ataques_pokemon
if st.button("Mostrar Ataques Pokémon"):
    ataques = obtener_ataques()
    if not ataques.empty:
        st.write("Ataques en la base de datos:")
        st.dataframe(ataques)
    else:
        st.write("No hay ataques en la base de datos.")

# Agregar un nuevo ataque
st.subheader("Agregar un nuevo ataque Pokémon")
nombre = st.text_input("Nombre del ataque")
tipo = st.selectbox("Tipo del ataque", ["Fuego", "Agua", "Planta", "Eléctrico", "Roca", "Acero", "Normal"])  # Agrega los tipos que desees
potencia = st.number_input("Potencia", min_value=0, step=1)
precision = st.number_input("Precisión", min_value=0, max_value=100, step=1)

if st.button("Agregar Ataque"):
    if nombre and tipo:
        agregar_ataque(nombre, tipo, potencia, precision)
        st.success("¡Ataque agregado exitosamente!")
    else:
        st.error("Todos los campos son obligatorios.")