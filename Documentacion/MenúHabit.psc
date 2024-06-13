Algoritmo GestionDeHabitos
    OP <- 0
    DNI <- ""
    Nombre <- ""
    CategoriaHabito <- ""
    Habito <- ""
    FechaInicio <- ""
    Detalles <- ""
    
    Repetir
        // Mostrar menú
        Limpiar Pantalla
        Escribir "Menú Principal"
        Escribir "   1. Crear Usuario"
        Escribir "   2. Modificar Usuario"
        Escribir "   3. Perfiles Guardados"
        Escribir "   4. Salir"
        // Ingresar una opción
        Escribir "Elija una opción (1-4): "
        Leer OP
        // Procesar esa opción
        Segun OP Hacer
            1:
                // Crear usuario
                Escribir "Crear Usuario"
                // Ingresar DNI
                Escribir "Ingrese su DNI:"
                Leer DNI
                // Ingresar Nombre
                Escribir "Ingrese su Nombre:"
                Leer Nombre
                // Ingresar Categoría de Hábito
                Escribir "Ingrese la Categoría de Hábito:"
                Leer CategoriaHabito
                // Ingresar Hábito
                Escribir "Ingrese el Hábito:"
                Leer Habito
                // Ingresar Fecha de Inicio
                Escribir "Ingrese la Fecha de Inicio:"
                Leer FechaInicio
                // Ingresar Detalles
                Escribir "Ingrese los Detalles:"
                Leer Detalles
            2:
                // Modificar usuario
                Escribir "Modificar Usuario"
                // Solicitar DNI
                Escribir "Ingrese el DNI del usuario a modificar:"
                Leer DNI
                // Verificar si el usuario existe
                Si DNI = DNI Entonces
                    // Ingresar Nombre
                    Escribir "Ingrese el nuevo Nombre o presione Enter para mantener el antiguo:"
                    Leer NuevoNombre
                    Si NuevoNombre <> "" Entonces
                        Nombre <- NuevoNombre
                    FinSi
                    // Ingresar Categoría de Hábito
                    Escribir "Ingrese la nueva Categoría de Hábito o presione Enter para mantener la antigua:"
                    Leer NuevaCategoriaHabito
                    Si NuevaCategoriaHabito <> "" Entonces
                        CategoriaHabito <- NuevaCategoriaHabito
                    FinSi
                    // Ingresar Hábito
                    Escribir "Ingrese el nuevo Hábito o presione Enter para mantener el antiguo:"
                    Leer NuevoHabito
                    Si NuevoHabito <> "" Entonces
                        Habito <- NuevoHabito
                    FinSi
                    // Ingresar Fecha de Inicio
                    Escribir "Ingrese la nueva Fecha de Inicio o presione Enter para mantener la antigua:"
                    Leer NuevaFechaInicio
                    Si NuevaFechaInicio <> "" Entonces
                        FechaInicio <- NuevaFechaInicio
                    FinSi
                    // Ingresar Detalles
                    Escribir "Ingrese los nuevos Detalles o presione Enter para mantener los antiguos:"
                    Leer NuevosDetalles
                    Si NuevosDetalles <> "" Entonces
                        Detalles <- NuevosDetalles
                    FinSi
                    Escribir "Usuario modificado exitosamente."
                Sino
                    Escribir "No se encontró ningún perfil asociado a ese DNI."
                FinSi
            3:
                // Perfiles guardados
                Escribir "Perfiles Guardados"
                // Solicitar DNI
                Escribir "Ingrese el DNI del usuario:"
                Leer DNI
                // Mostrar perfil relacionado al DNI
                Si DNI = DNI Entonces
                    Escribir "DNI: ", DNI
                    Escribir "Nombre: ", Nombre
                    Escribir "Categoría de Hábito: ", CategoriaHabito
                    Escribir "Hábito: ", Habito
                    Escribir "Fecha de Inicio: ", FechaInicio
                    Escribir "Detalles: ", Detalles
                Sino
                    Escribir "No se encontró ningún perfil asociado a ese DNI."
                FinSi
            4:
                // Salir
                Escribir "Saliendo del programa."
            De otro modo:
                Escribir "Opción no válida"
        FinSegun
        Escribir "Presione enter para continuar"
        Esperar Tecla
    Hasta Que OP = 4
FinAlgoritmo
