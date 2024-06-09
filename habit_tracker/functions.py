from models import User
from utils import get_input
from validations import (
    validate_username,
    validate_email,
    validate_password
)

# Registra un nuevo usuario y lo añade a la lista de usuarios
def register_user(users):
    print("\n╭──────────────────────────────────────╮")
    print("\t   REGISTRAR USUARIO")
    print("╰──────────────────────────────────────╯\n")
    
    # Obtener y validar nombre de usuario
    while True:
        username = get_input("➤ Ingrese nombre de usuario: ")
        valid, error = validate_username(username)
        if valid:
            break
        print(error)

    # Obtener y validar correo electrónico
    while True:
        email = get_input("➤ Ingrese correo electrónico: ")
        valid, error = validate_email(email)
        if valid:
            break
        print(error)

    # Obtener y validar contraseña
    while True:
        password = get_input("➤ Ingrese contraseña: ")
        valid, error = validate_password(password)
        if valid:
            break
        print(error)
    
    user = User(username, email, password)
    users.append(user)
    print("\n¡Usuario registrado exitosamente!\n")


# Inicia sesión para un usuario existente y devuelve el usuario si es exitoso
def login(users):
    print("\n╭──────────────────────────────────────╮")
    print("\t     INICIAR SESIÓN")
    print("╰──────────────────────────────────────╯\n")
    username = get_input("Ingrese nombre de usuario: ")
    password = get_input("Ingrese contraseña: ")
    for user in users:
        if user.username == username and user.password == password:
            print(f"¡Usuario {user.username} inició sesión exitosamente!")
            return user
    print("Nombre de usuario o contraseña incorrectos.")
    return None