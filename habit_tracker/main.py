from db_connection import create_connection, close_connection
from user_management import register_user, login
from functions import (
    view_profile, 
    manage_categories, 
    manage_habits, 
    manage_logs,
    mostrar_habitos_usuario,
    filtrar_habitos_por_categoria,
    obtener_registros_habito,
    obtener_tiempo_total_habito,
    mostrar_habitos_y_categorias,
    mostrar_habitos_con_multiples_registros,
    filtrar_registros_por_fecha
)
from utils import print_menu

PURPLE = '\033[95m'
print(PURPLE)

current_user = None

def main_menu():
    global current_user
    while True:
        print("\n●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●")
        print("\t    MENU PRINCIPAL")
        print("●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●")
        choice = print_menu(
            [
                "Ver Perfil",
                "Gestionar Categorías",
                "Gestionar Hábitos",
                "Gestionar Registros",
                "Cerrar Sesión",
            ]
        )
        if choice == 1:
            view_profile(current_user[0])
        elif choice == 2:
            manage_categories(current_user[0])
        elif choice == 3:
            manage_habits(current_user[0])
        elif choice == 4:
            manage_logs(current_user[0])
        elif choice == 5:
            print("\n●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●")
            print("\t   Ha cerrado sesión")
            print("●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●\n")
            break

def admin_menu():
    while True:
        print("\n●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●")
        print("\t    MENU ADMINISTRADOR")
        print("●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●\n")
        choice = print_menu(
            [
                "Mostrar hábitos de usuario",
                "Filtrar hábitos por categoría",
                "Obtener registros de hábitos para un hábito específico",
                "Obtener tiempo total dedicado a un hábito",
                "Mostrar hábitos y sus categorías",
                "Mostrar hábitos con múltiples registros",
                "Filtrar registros de hábitos por fecha",
                "Volver al menú principal",
            ]
        )
        if choice == 1:
            user_id = input("Ingrese el ID del usuario: ")
            resultados = mostrar_habitos_usuario(user_id)
            for resultado in resultados:
                print(resultado)
        elif choice == 2:
            category_id = input("Ingrese el ID de la categoría: ")
            resultados = filtrar_habitos_por_categoria(category_id)
            for resultado in resultados:
                print(resultado)
        elif choice == 3:
            user_id = input("Ingrese el ID del usuario: ")
            habit_id = input("Ingrese el ID del hábito: ")
            resultados = obtener_registros_habito(user_id, habit_id)
            for resultado in resultados:
                print(resultado)
        elif choice == 4:
            habit_id = input("Ingrese el ID del hábito: ")
            total_duracion = obtener_tiempo_total_habito(habit_id)
            print(f"Tiempo total dedicado: {total_duracion} minutos")
        elif choice == 5:
            resultados = mostrar_habitos_y_categorias()
            for resultado in resultados:
                print(resultado)
        elif choice == 6:
            resultados = mostrar_habitos_con_multiples_registros()
            for resultado in resultados:
                print(resultado)
        elif choice == 7:
            start_date = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
            end_date = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
            resultados = filtrar_registros_por_fecha(start_date, end_date)
            for resultado in resultados:
                print(resultado)
        elif choice == 8:
            break
        else:
            print("\nOpción inválida, por favor intente nuevamente.")
            continue

def main():
    global current_user
    while True:
        print("┌─────────────── ⋆⋅ ☆ ⋅⋆ ───────────────┐")
        print("\t  SEGUIMIENTO DE HÁBITOS")
        print("└─────────────── ⋆⋅ ☆ ⋅⋆ ───────────────┘")
        choice = print_menu(["Registro de Usuario", "Iniciar Sesión", "Iniciar Sesión como Administrador", "Salir"])
        if choice == 1:
            register_user()
        elif choice == 2:
            current_user = login()                        
            if current_user:
                main_menu()
            else:
                print("\n⚠️ Inicio de sesión fallido, intente nuevamente.\n")
        elif choice == 3:
            admin_user = input("\n➤ Ingrese el usuario administrador: ")
            admin_password = input("➤ Ingrese la contraseña del administrador: ")
            if admin_user == 'admin' and admin_password == 'admin':
                admin_menu()
            else:
                print("⚠️ Usuario o contraseña incorrectos.")
        elif choice == 4:
            print("\n●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●")
            print("\tHa salido del programa")
            print("●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●\n")
            break

if __name__ == "__main__":
    main()
