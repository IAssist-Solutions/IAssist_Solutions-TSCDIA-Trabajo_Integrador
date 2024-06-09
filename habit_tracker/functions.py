from models import User, Category, Habit, HabitLog
from utils import get_input, print_menu

users = []
current_user = None

def register_user():
    print("Register User")
    username = get_input("Enter username: ")
    email = get_input("Enter email: ")
    password = get_input("Enter password: ")
    user = User(username, email, password)
    users.append(user)
    print("User registered successfully!")

def login():
    global current_user
    print("Login")
    username = get_input("Enter username: ")
    password = get_input("Enter password: ")
    for user in users:
        if user.username == username and user.password == password:
            current_user = user
            print("Login successful!")
            return
    print("Invalid username or password.")

def view_profile():
    print("Profile")
    print(current_user)

def manage_categories():
    while True:
        print("Categories")
        choice = print_menu(["View Categories", "Create Category", "Edit Category", "Delete Category", "Back to Main Menu"])
        if choice == 1:
            for category in current_user.categories:
                print(category)
        elif choice == 2:
            name = get_input("Enter category name: ")
            category = Category(name)
            current_user.categories.append(category)
            print("Category created successfully!")
        elif choice == 3:
            name = get_input("Enter category name to edit: ")
            for category in current_user.categories:
                if category.name == name:
                    new_name = get_input("Enter new category name: ")
                    category.name = new_name
                    print("Category updated successfully!")
                    break
            else:
                print("Category not found.")
        elif choice == 4:
            name = get_input("Enter category name to delete: ")
            for category in current_user.categories:
                if category.name == name:
                    current_user.categories.remove(category)
                    print("Category deleted successfully!")
                    break
            else:
                print("Category not found.")
        elif choice == 5:
            break

def manage_habits():
    while True:
        print("Habits")
        choice = print_menu(["View Habits", "Create Habit", "Edit Habit", "Delete Habit", "Back to Main Menu"])
        if choice == 1:
            for habit in current_user.habits:
                print(habit)
        elif choice == 2:
            name = get_input("Enter habit name: ")
            description = get_input("Enter habit description: ")
            start_date = get_input("Enter habit start date (YYYY-MM-DD): ")
            category_name = get_input("Enter category name for the habit: ")
            for category in current_user.categories:
                if category.name == category_name:
                    habit = Habit(name, description, start_date, category)
                    current_user.habits.append(habit)
                    print("Habit created successfully!")
                    break
            else:
                print("Category not found.")
        elif choice == 3:
            name = get_input("Enter habit name to edit: ")
            for habit in current_user.habits:
                if habit.name == name:
                    habit.name = get_input("Enter new habit name: ")
                    habit.description = get_input("Enter new habit description: ")
                    habit.start_date = get_input("Enter new habit start date (YYYY-MM-DD): ")
                    category_name = get_input("Enter new category name for the habit: ")
                    for category in current_user.categories:
                        if category.name == category_name:
                            habit.category = category
                            print("Habit updated successfully!")
                            break
                    else:
                        print("Category not found.")
                    break
            else:
                print("Habit not found.")
        elif choice == 4:
            name = get_input("Enter habit name to delete: ")
            for habit in current_user.habits:
                if habit.name == name:
                    current_user.habits.remove(habit)
                    print("Habit deleted successfully!")
                    break
            else:
                print("Habit not found.")
        elif choice == 5:
            break

def manage_logs():
    while True:
        print("Logs")
        choice = print_menu(["View Logs", "Add Log", "Back to Main Menu"])
        if choice == 1:
            for habit in current_user.habits:
                for log in habit.logs:
                    print(log)
        elif choice == 2:
            habit_name = get_input("Enter habit name: ")
            for habit in current_user.habits:
                if habit.name == habit_name:
                    log_date = get_input("Enter log date (YYYY-MM-DD): ")
                    description = get_input("Enter log description: ")
                    start_time = get_input("Enter log start time (HH:MM:SS): ")
                    end_time = get_input("Enter log end time (HH:MM:SS): ")
                    duration = int(get_input("Enter log duration in minutes: "))
                    log = HabitLog(log_date, description, start_time, end_time, duration)
                    habit.logs.append(log)
                    print("Log added successfully!")
                    break
            else:
                print("Habit not found.")
        elif choice == 3:
            break
