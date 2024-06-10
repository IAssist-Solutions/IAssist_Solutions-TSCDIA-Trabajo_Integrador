# Para solicitar y devolver la entrada del usuario, eliminando espacios al principio y al final
def get_input(prompt):
    return input(prompt).strip()

# Para imprimir un menú numerado basado en las opciones dadas y solicitar al usuario que elija una opción
def print_menu(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = input("\n➤ Elija una opción: ").strip()
    return int(choice) if choice.isdigit() and 1 <= int(choice) <= len(options) else None
