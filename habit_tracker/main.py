from utils import print_menu
from functions import login, register_user
from user_management import view_profile, manage_categories, manage_habits, manage_logs
PURPLE = '\033[95m'
print(PURPLE)

users = []
current_user = None

def main_menu():
    global current_user
    while True:
        print("●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●")
        print("\t    MENU PRINCIPAL")
        print("●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●\n")
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
            view_profile(current_user)
        elif choice == 2:
            manage_categories(current_user)
        elif choice == 3:
            manage_habits(current_user)
        elif choice == 4:
            manage_logs(current_user)
        elif choice == 5:
            break

def main():
    global current_user
    while True:
        print("┌─────────────── ⋆⋅ ☆ ⋅⋆ ───────────────┐")
        print("\t  SEGUIMIENTO DE HÁBITOS")
        print("└─────────────── ⋆⋅ ☆ ⋅⋆ ───────────────┘\n")
        choice = print_menu(["Registro de Usuario", "Iniciar Sesión", "Salir"])
        if choice == 1:
            register_user(users)
        elif choice == 2:
            current_user = login(users)                        
            if current_user:
                main_menu()
            else:
                print("\n⚠️ Inicio de sesión fallido, intente nuevamente.\n")
        elif choice == 3:
            break

if __name__ == "__main__":
    main()