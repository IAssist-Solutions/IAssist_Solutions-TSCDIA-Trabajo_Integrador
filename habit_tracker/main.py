from utils import print_menu
from functions import (
    register_user,
    login,
    view_profile,
    manage_categories,
    manage_habits,
    manage_logs,
    users,
    current_user
)

def main_menu():
    while True:
        print("Main Menu")
        choice = print_menu(["View Profile", "Manage Categories", "Manage Habits", "Manage Logs", "Logout"])
        if choice == 1:
            view_profile()
        elif choice == 2:
            manage_categories()
        elif choice == 3:
            manage_habits()
        elif choice == 4:
            manage_logs()
        elif choice == 5:
            break

def main():
    while True:
        print("Habit Tracker")
        choice = print_menu(["Register User", "Login", "Exit"])
        if choice == 1:
            register_user()
        elif choice == 2:
            login()
            if current_user:
                main_menu()
        elif choice == 3:
            break

if __name__ == "__main__":
    main()