from utils_old import get_input, print_menu
from models_old import Category, Habit, HabitLog

# Para ver datos del Usuario creado
def view_profile(current_user):
    print("\n╭──────────────────────────────────────╮")
    print("\t       PERFIL")
    print("╰──────────────────────────────────────╯\n")
    print(current_user)

# Gestiona las categorías del usuario actual
def manage_categories(current_user):
    while True:
        print("\n╭──────────────────────────────────────╮")
        print("\t      CATEGORIAS")
        print("╰──────────────────────────────────────╯\n")
        choice = print_menu(["Ver Categorías", "Crear Categoría", "Editar Categoría", "Eliminar Categoría", "Volver al Menú Principal"])
        if choice == 1:
            for category in current_user.categories:
                print(category)
        elif choice == 2:
            name = get_input("\n➤ Ingrese nombre de la categoría: ")
            category = Category(name)
            current_user.categories.append(category)
            print("\n¡Categoría creada exitosamente!\n")
        elif choice == 3:
            name = get_input("\n➤ Ingrese nombre de la categoría a editar: ")
            for category in current_user.categories:
                if category.name == name:
                    new_name = get_input("➤ Ingrese nuevo nombre de la categoría: ")
                    category.name = new_name
                    print("\n¡Categoría actualizada exitosamente!\n")
                    break
            else:
                print("\nCategoría no encontrada.\n")
        elif choice == 4:
            name = get_input("\n➤ Ingrese nombre de la categoría a eliminar: ")
            for category in current_user.categories:
                if category.name == name:
                    current_user.categories.remove(category)
                    print("\n¡Categoría eliminada exitosamente!\n")
                    break
            else:
                print("\nCategoría no encontrada.\n")
        elif choice == 5:
            break

# Gestiona los hábitos del usuario actual
def manage_habits(current_user):
    while True:
        print("\nHÁBITOS\n")
        choice = print_menu(["Ver Hábitos", "Crear Hábito", "Editar Hábito", "Eliminar Hábito", "Volver al Menú Principal"])
        if choice == 1:
            for habit in current_user.habits:
                print(habit)
        elif choice == 2:
            name = get_input("\n➤ Ingrese nombre del hábito: ")
            description = get_input("➤ Ingrese descripción del hábito: ")
            start_date = get_input("➤ Ingrese fecha de inicio del hábito (YYYY-MM-DD): ")
            category_name = get_input("➤ Ingrese nombre de la categoría para el hábito: ")
            for category in current_user.categories:
                if category.name == category_name:
                    habit = Habit(name, description, start_date, category)
                    current_user.habits.append(habit)
                    print("\n¡Hábito creado exitosamente!\n")
                    break
            else:
                print("\nCategoría no encontrada.\n")
        elif choice == 3:
            name = get_input("\n➤ Ingrese nombre del hábito a editar: ")
            for habit in current_user.habits:
                if habit.name == name:
                    habit.name = get_input("➤ Ingrese nuevo nombre del hábito: ")
                    habit.description = get_input("➤ Ingrese nueva descripción del hábito: ")
                    habit.start_date = get_input("➤ Ingrese nueva fecha de inicio del hábito (YYYY-MM-DD): ")
                    category_name = get_input("➤ Ingrese nuevo nombre de la categoría para el hábito: ")
                    for category in current_user.categories:
                        if category.name == category_name:
                            habit.category = category
                            print("\n¡Hábito actualizado exitosamente!\n")
                            break
                    else:
                        print("\nCategoría no encontrada.\n")
                    break
            else:
                print("\nHábito no encontrado.\n")
        elif choice == 4:
            name = get_input("\n➤ Ingrese nombre del hábito a eliminar: ")
            for habit in current_user.habits:
                if habit.name == name:
                    current_user.habits.remove(habit)
                    print("\n¡Hábito eliminado exitosamente!\n")
                    break
            else:
                print("\nHábito no encontrado.\n")
        elif choice == 5:
            print("\nVolviendo al menu principal...\n")
            break

# Gestiona los registros de los hábitos del usuario actual
def manage_logs(current_user):
    while True:
        print("\nREGISTROS\n")
        choice = print_menu(["Ver Registros", "Añadir Registro", "Volver al Menú Principal"])
        if choice == 1:
            for habit in current_user.habits:
                for log in habit.logs:
                    print(log)
        elif choice == 2:
            habit_name = get_input("➤ Ingrese nombre del hábito: ")
            for habit in current_user.habits:
                if habit.name == habit_name:
                    log_date = get_input("➤ Ingrese fecha del registro (YYYY-MM-DD): ")
                    description = get_input("➤ Ingrese descripción del registro: ")
                    start_time = get_input("➤ Ingrese hora de inicio del registro (HH:MM:SS): ")
                    end_time = get_input("➤ Ingrese hora de finalización del registro (HH:MM:SS): ")
                    duration = int(get_input("➤ Ingrese duración del registro en minutos: "))
                    log = HabitLog(log_date, description, start_time, end_time, duration)
                    habit.logs.append(log)
                    print("\n¡Registro añadido exitosamente!\n")
                    break
            else:
                print("\nHábito no encontrado.\n")
        elif choice == 3:
            break