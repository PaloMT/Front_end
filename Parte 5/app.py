from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuración de conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host="192.168.1.17",
        user="GP_G3",  # Sustituid con vuestro usuario
        password="segura_GP_G3",  # Sustituid con vuestra contraseña
        database="Estudio_CCII_GP_G3"  # Sustituid con vuestra base de datos
    )

# Ruta principal para prueba
@app.route('/test', methods=['GET'])
def test_connection():
   try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    database_name = cursor.fetchone()
    return jsonify({"success": True, "database": database_name[0]})
   except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


# Ruta para agregar un alumno
@app.route('/add', methods=['POST'])
def add_student():
    try:
      data = request.json
      conn = get_db_connection()
      cursor = conn.cursor()
      query = "INSERT INTO alumno (id, nombre_alumno, clase) VALUES (%s, %s, %s)"
      cursor.execute(query, (data['id'], data['nombre_alumno'], data['clase']))
      conn.commit()
      return jsonify({"success": True, "message": "Alumno agregado correctamente"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# Ruta para listar alumnos
@app.route('/students', methods=['GET'])
def get_students():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM alumno")
        students = cursor.fetchall()
        return jsonify(students)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)
