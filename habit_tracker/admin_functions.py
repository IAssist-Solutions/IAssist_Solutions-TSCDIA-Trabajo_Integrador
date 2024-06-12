from db_connection import create_connection, close_connection

def mostrar_habitos_usuario(conexion, user_id):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM habit WHERE user_id = ?", (user_id,))
    resultados = cursor.fetchall()
    return resultados

def filtrar_habitos_por_categoria(conexion, category_id):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM habit WHERE category_id = ?", (category_id,))
    resultados = cursor.fetchall()
    return resultados

def obtener_registros_habito(conexion, user_id, habit_id):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM habitlog WHERE user_id = ? AND habit_id = ?", (user_id, habit_id))
    resultados = cursor.fetchall()
    return resultados

def obtener_tiempo_total_habito(conexion, habit_id):
    cursor = conexion.cursor()
    cursor.execute("SELECT SUM(duration) AS total_duracion FROM habitlog WHERE habit_id = ?", (habit_id,))
    resultado = cursor.fetchone()
    return resultado['total_duracion']

def mostrar_habitos_y_categorias(conexion):
    cursor = conexion.cursor()
    cursor.execute("""
    SELECT h.name, c.category_name
    FROM habit h
    INNER JOIN category c ON h.category_id = c.category_id
    """)
    resultados = cursor.fetchall()
    return resultados

def mostrar_habitos_con_multiples_registros(conexion):
    cursor = conexion.cursor()
    cursor.execute("""
    SELECT h.name, COUNT(l.log_id) AS total_logs
    FROM habit h
    INNER JOIN habitlog l ON h.habit_id = l.habit_id
    GROUP BY h.habit_id
    HAVING COUNT(l.log_id) > 1
    """)
    resultados = cursor.fetchall()
    return resultados

def filtrar_registros_por_fecha(conexion, start_date, end_date):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM habitlog WHERE log_date BETWEEN ? AND ?", (start_date, end_date))
    resultados = cursor.fetchall()
    return resultados
