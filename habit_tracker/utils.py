def print_header(title):
    print("\n" + "="*len(title))
    print(title)
    print("="*len(title) + "\n")

def print_menu(options):
    print_header("Seleccione una opción")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("\nIngrese el número de la opción deseada: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Opción inválida. Por favor, intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")