from db_connection import create_connection, close_connection

# Función para ver el perfil del usuario
def view_profile(user_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()        
        cursor.execute(f"SELECT username, email FROM user WHERE user_id = {user_id}")
        user = cursor.fetchone()
        if user:
            print("\n╭──────────────────────────────────────╮")
            print("\t        TU PERFIL")
            print("╰──────────────────────────────────────╯\n")
            print(f"Nombre de usuario: {user[0]}")
            print(f"Correo electrónico: {user[1]}")
        close_connection(connection)

# Función para gestionar categorías
def manage_categories(user_id):
    while True:
        print("\n╭──────────────────────────────────────╮")
        print("\t     MENU CATEGORIAS")
        print("╰──────────────────────────────────────╯\n")        
        print("1. Ver todas las categorías")
        print("2. Agregar nueva categoría")
        print("3. Editar categoría existente")
        print("4. Eliminar categoría")
        print("5. Volver al menú principal")
        choice = input("\n➤ Ingrese su opción: ")

        if choice == '1':
            view_categories()
        elif choice == '2':
            add_category()
        elif choice == '3':
            edit_category()
        elif choice == '4':
            delete_category()
        elif choice == '5':
            break
        else:
            print("Opción inválida, por favor intente nuevamente.")

def view_categories():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM category")
        categories = cursor.fetchall()
        print("CATEGORIAS DISPONIBLES:")
        for category in categories:
            print(f"{category[0]}: {category[1]}")
        close_connection(connection)

def add_category():
    print("\nNUEVA CATEGORIA:")
    category_name = input("\n➤ Ingrese el nombre de la categoría: ")
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO category (category_name) VALUES ('{category_name}')")
        connection.commit()
        print("Categoría agregada exitosamente.")
        close_connection(connection)

def edit_category():
    print("\nEDICIÓN DE CATEGORIA:")
    category_id = input("\n➤ Ingrese el ID de la categoría a editar(Nro): ")
    new_category_name = input("➤ Ingrese el nuevo nombre de la categoría: ")
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(f"UPDATE category SET category_name = '{new_category_name}' WHERE category_id = {category_id}")
        connection.commit()
        print("Categoría editada exitosamente.")
        close_connection(connection)

def delete_category():
    print("\nBORRADO DE CATEGORIA:")
    category_id = input("\n➤ Ingrese el ID de la categoría a eliminar(Nro): ")
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM category WHERE category_id = {category_id}")
        connection.commit()
        print("Categoría eliminada exitosamente.")
        close_connection(connection)

# Función para gestionar hábitos
def manage_habits(user_id):
    while True:
        print("\n╭──────────────────────────────────────╮")
        print("\t MENU DE HABITOS")
        print("╰──────────────────────────────────────╯\n")         
        print("1. Ver todos los hábitos")
        print("2. Agregar nuevo hábito")
        print("3. Editar hábito existente")
        print("4. Eliminar hábito")
        print("5. Volver al menú principal")
        choice = input("\n➤ Ingrese su opción: ")

        if choice == '1':
            view_habits(user_id)
        elif choice == '2':
            add_habit(user_id)
        elif choice == '3':
            edit_habit()
        elif choice == '4':
            delete_habit()
        elif choice == '5':
            break
        else:
            print("\nOpción inválida, por favor intente nuevamente.")

def view_habits(user_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM habit WHERE user_id = {user_id}")
        habits = cursor.fetchall()
        for habit in habits:
            print(f"{habit[0]}: {habit[1]} - {habit[2]}")
        close_connection(connection)

def add_habit(user_id):
    name = input("➤ Ingrese el nombre del hábito: ")
    description = input("➤ Ingrese la descripción del hábito: ")
    start_date = input("➤ Ingrese la fecha de inicio (YYYY-MM-DD): ")
    category_id = input("➤ Ingrese el ID de la categoría(Nro): ")
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO habit (name, description, start_date, category_id, user_id) VALUES ('{name}', '{description}', '{start_date}', {category_id}, {user_id})")
        connection.commit()
        print("\nHábito agregado exitosamente.")
        close_connection(connection)

def edit_habit():
    habit_id = input("➤ Ingrese el ID del hábito a editar(Nro): ")
    new_name = input("➤ Ingrese el nuevo nombre del hábito: ")
    new_description = input("➤ Ingrese la nueva descripción del hábito: ")
    new_start_date = input("➤ Ingrese la nueva fecha de inicio (YYYY-MM-DD): ")
    new_category_id = input("➤ Ingrese el nuevo ID de la categoría: ")
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(f"UPDATE habit SET name = '{new_name}', description = '{new_description}', start_date = '{new_start_date}', category_id = {new_category_id} WHERE habit_id = {habit_id}")
        connection.commit()
        print("\nHábito editado exitosamente.")
        close_connection(connection)

def delete_habit():
    habit_id = input("➤ Ingrese el ID del hábito a eliminar(Nro): ")
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM habit WHERE habit_id = {habit_id}")
        connection.commit()
        print("\nHábito eliminado exitosamente.")
        close_connection(connection)

# Función para gestionar registros de hábitos
def manage_logs(user_id):
    while True:
        print("\n╭──────────────────────────────────────╮")
        print("\t   MENU DE REGISTROS")
        print("╰──────────────────────────────────────╯\n")        
        print("1. Ver todos los registros")
        print("2. Agregar nuevo registro")
        print("3. Editar registro existente")
        print("4. Eliminar registro")
        print("5. Volver al menú principal")
        choice = input("➤ Ingrese su opción: ")

        if choice == '1':
            view_logs(user_id)
        elif choice == '2':
            add_log(user_id)
        elif choice == '3':
            edit_log()
        elif choice == '4':
            delete_log()
        elif choice == '5':
            break
        else:
            print("\nOpción inválida, por favor intente nuevamente.")

def view_logs(user_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM habitlog WHERE user_id = {user_id}")
        logs = cursor.fetchall()
        for log in logs:
            print(f"{log[0]}: {log[2]} - {log[3]} a {log[4]}, {log[5]} minutos")
        close_connection(connection)

def add_log(user_id):
    log_date = input("➤ Ingrese la fecha del registro (YYYY-MM-DD): ")
    description = input("➤ Ingrese la descripción del registro: ")
    start_time = input("➤ Ingrese la hora de inicio (HH:MM:SS): ")
    end_time = input("➤ Ingrese la hora de finalización (HH:MM:SS): ")
    duration = int(input("➤ Ingrese la duración en minutos: "))
    habit_id = input("➤ Ingrese el ID del hábito(Nro): ")
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO habitlog (log_date, description, start_time, end_time, duration, user_id, habit_id) VALUES ('{log_date}', '{description}', '{start_time}', '{end_time}', {duration}, {user_id}, {habit_id})")
        connection.commit()
        print("\nRegistro agregado exitosamente.")
        close_connection(connection)

def edit_log():
    log_id = input("➤ Ingrese el ID del registro a editar(Nro): ")
    new_log_date = input("➤ Ingrese la nueva fecha del registro (YYYY-MM-DD): ")
    new_description = input("➤ Ingrese la nueva descripción del registro: ")
    new_start_time = input("➤ Ingrese la nueva hora de inicio (HH:MM:SS): ")
    new_end_time = input("➤ Ingrese la nueva hora de finalización (HH:MM:SS): ")
    new_duration = int(input("➤ Ingrese la nueva duración en minutos: "))
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(f"UPDATE habitlog SET log_date = '{new_log_date}', description = '{new_description}', start_time = '{new_start_time}', end_time = '{new_end_time}', duration = {new_duration} WHERE log_id = {log_id}")
        connection.commit()
        print("\nRegistro editado exitosamente.")
        close_connection(connection)

def delete_log():
    log_id = input("➤ Ingrese el ID del registro a eliminar(Nro): ")
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM habitlog WHERE log_id = {log_id}")
        connection.commit()
        print("\nRegistro eliminado exitosamente.")
        close_connection(connection)