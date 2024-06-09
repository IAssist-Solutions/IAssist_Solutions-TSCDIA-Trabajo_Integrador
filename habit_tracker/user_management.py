from utils import get_input, print_menu
from models import Category, Habit, HabitLog

def view_profile(current_user):
    print("Perfil")
    print(current_user)

def manage_categories(current_user):
    while True:
        print("Categorías")
        choice = print_menu(["Ver Categorías", "Crear Categoría", "Editar Categoría", "Eliminar Categoría", "Volver al Menú Principal"])
        if choice == 1:
            for category in current_user.categories:
                print(category)
        elif choice == 2:
            name = get_input("Ingrese nombre de la categoría: ")
            category = Category(name)
            current_user.categories.append(category)
            print("¡Categoría creada exitosamente!")
        elif choice == 3:
            name = get_input("Ingrese nombre de la categoría a editar: ")
            for category in current_user.categories:
                if category.name == name:
                    new_name = get_input("Ingrese nuevo nombre de la categoría: ")
                    category.name = new_name
                    print("¡Categoría actualizada exitosamente!")
                    break
            else:
                print("Categoría no encontrada.")
        elif choice == 4:
            name = get_input("Ingrese nombre de la categoría a eliminar: ")
            for category in current_user.categories:
                if category.name == name:
                    current_user.categories.remove(category)
                    print("¡Categoría eliminada exitosamente!")
                    break
            else:
                print("Categoría no encontrada.")
        elif choice == 5:
            break

def manage_habits(current_user):
    while True:
        print("Hábitos")
        choice = print_menu(["Ver Hábitos", "Crear Hábito", "Editar Hábito", "Eliminar Hábito", "Volver al Menú Principal"])
        if choice == 1:
            for habit in current_user.habits:
                print(habit)
        elif choice == 2:
            name = get_input("Ingrese nombre del hábito: ")
            description = get_input("Ingrese descripción del hábito: ")
            start_date = get_input("Ingrese fecha de inicio del hábito (YYYY-MM-DD): ")
            category_name = get_input("Ingrese nombre de la categoría para el hábito: ")
            for category in current_user.categories:
                if category.name == category_name:
                    habit = Habit(name, description, start_date, category)
                    current_user.habits.append(habit)
                    print("¡Hábito creado exitosamente!")
                    break
            else:
                print("Categoría no encontrada.")
        elif choice == 3:
            name = get_input("Ingrese nombre del hábito a editar: ")
            for habit in current_user.habits:
                if habit.name == name:
                    habit.name = get_input("Ingrese nuevo nombre del hábito: ")
                    habit.description = get_input("Ingrese nueva descripción del hábito: ")
                    habit.start_date = get_input("Ingrese nueva fecha de inicio del hábito (YYYY-MM-DD): ")
                    category_name = get_input("Ingrese nuevo nombre de la categoría para el hábito: ")
                    for category in current_user.categories:
                        if category.name == category_name:
                            habit.category = category
                            print("¡Hábito actualizado exitosamente!")
                            break
                    else:
                        print("Categoría no encontrada.")
                    break
            else:
                print("Hábito no encontrado.")
        elif choice == 4:
            name = get_input("Ingrese nombre del hábito a eliminar: ")
            for habit in current_user.habits:
                if habit.name == name:
                    current_user.habits.remove(habit)
                    print("¡Hábito eliminado exitosamente!")
                    break
            else:
                print("Hábito no encontrado.")
        elif choice == 5:
            break

def manage_logs(current_user):
    while True:
        print("Registros")
        choice = print_menu(["Ver Registros", "Añadir Registro", "Volver al Menú Principal"])
        if choice == 1:
            for habit in current_user.habits:
                for log in habit.logs:
                    print(log)
        elif choice == 2:
            habit_name = get_input("Ingrese nombre del hábito: ")
            for habit in current_user.habits:
                if habit.name == habit_name:
                    log_date = get_input("Ingrese fecha del registro (YYYY-MM-DD): ")
                    description = get_input("Ingrese descripción del registro: ")
                    start_time = get_input("Ingrese hora de inicio del registro (HH:MM:SS): ")
                    end_time = get_input("Ingrese hora de finalización del registro (HH:MM:SS): ")
                    duration = int(get_input("Ingrese duración del registro en minutos: "))
                    log = HabitLog(log_date, description, start_time, end_time, duration)
                    habit.logs.append(log)
                    print("¡Registro añadido exitosamente!")
                    break
            else:
                print("Hábito no encontrado.")
        elif choice == 3:
            break