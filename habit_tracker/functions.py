from models import User
from utils import get_input

def register_user(users):
    print("Registrar Usuario")
    username = get_input("Ingrese nombre de usuario: ")
    email = get_input("Ingrese correo electrónico: ")
    password = get_input("Ingrese contraseña: ")
    user = User(username, email, password)
    users.append(user)
    print("¡Usuario registrado exitosamente!")

def login(users):
    print("Iniciar Sesión")
    username = get_input("Ingrese nombre de usuario: ")
    password = get_input("Ingrese contraseña: ")
    for user in users:
        if user.username == username and user.password == password:
            print(f"¡Usuario {user.username} inició sesión exitosamente!")
            return user
    print("Nombre de usuario o contraseña incorrectos.")
    return None