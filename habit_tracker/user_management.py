import bcrypt
from db_connection import create_connection, close_connection

def register_user():
    username = input("Ingrese su nombre de usuario: ")
    email = input("Ingrese su correo electrónico: ")
    password = input("Ingrese su contraseña: ")
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO user (username, email, password) VALUES (%s, %s, %s)", (username, email, hashed_password))
        connection.commit()
        print("Usuario registrado exitosamente.")
        close_connection(connection)

def login():
    email = input("Ingrese su correo electrónico: ")
    password = input("Ingrese su contraseña: ")

    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user WHERE email = %s", (email,))
        user = cursor.fetchone()
        if user and bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):
            print("Inicio de sesión exitoso.")
            close_connection(connection)
            return user
        else:
            print("Correo electrónico o contraseña incorrectos.")
            close_connection(connection)
            return None