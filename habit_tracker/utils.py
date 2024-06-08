def get_input(prompt):
    return input(prompt).strip()


def print_menu(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = input("Choose an option: ").strip()
    return int(choice) if choice.isdigit() and 1 <= int(choice) <= len(options) else None
