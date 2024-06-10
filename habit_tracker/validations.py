import re

#Validaciones de los inputs que carga por teclado el usuario

def validate_username(username):
    if not username.isalpha():
        return False, "El nombre debe contener solo letras"
    return True, ""

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        return False, "Email invalido"
    return True, ""

def validate_password(password):
    if len(password) < 8 or len(password) > 100:
        return False, "La clave debe tener entre 8 y 100 caracteres."
    if ' ' in password:
        return False, "No se permiten espacios en la clave"
    return True, ""

def validate_date(date):
    date_regex = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(date_regex, date):
        return False, "La fecha debe tener formato AAAA-MM-DD."
    return True, ""

def validate_time(time):
    time_regex = r'^\d{2}:\d{2}:\d{2}$'
    if not re.match(time_regex, time):
        return False, "La hora debe tener formato HH:MM:SS."
    return True, ""

def validate_duration(duration):
    if not duration.isdigit() or int(duration) <= 0:
        return False, "La duración debe ser un número positivo."
    return True, ""