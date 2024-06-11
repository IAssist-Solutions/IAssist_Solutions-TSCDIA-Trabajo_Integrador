from user_management import register_user, login
from functions import view_profile, manage_categories, manage_habits, manage_logs
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
                "Ver Usuarios",
                "Eliminar Usuario",
                "Volver al Menú Principal",
            ]
        )
        if choice == 1:
            # Implementar la lógica para ver usuarios
            pass
        elif choice == 2:
            # Implementar la lógica para eliminar usuarios
            pass
        elif choice == 3:
            break

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