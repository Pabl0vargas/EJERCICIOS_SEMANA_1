#registro_estudiantes
# Diccionario principal
estudiantes = {}

def agregar_estudiante():
    nombre = input("\nIngrese el nombre del estudiante: ")
    if nombre in estudiantes:
        print("\nEse estudiante ya existe.")
        return
    try:
        edad = int(input("Edad: "))
        calificacion = float(input("Calificación: "))
        estudiantes[nombre] = {'edad': edad, 'calificacion': calificacion}
        print(f"\nEstudiante {nombre} agregado correctamente.\n")
    except ValueError:
        print("\nEdad o calificación no válidas.\n")


def modificar_calificacion():
    nombre = input("\n Ingrese el nombre del estudiante: ")
    if nombre in estudiantes:
        try:
            nueva_calificacion = float(input("Nueva calificación: "))

            estudiantes[nombre]['calificacion'] = nueva_calificacion
            print(f"\nCalificación actualizada para {nombre}.\n")
        except ValueError:
            print("\nCalificación no válida.\n")
    else:
        print("\nEstudiante no encontrado.\nIngrese una opcion nuevamente\n")

def mostrar_estudiantes():
    if not estudiantes:
        print("\nNo hay estudiantes registrados.\n")
    else:
        print("\nLista de estudiantes:")
        for nombre, datos in estudiantes.items():
            print(f"\n|Nombre: {nombre}| Edad: {datos['edad']}| Calificación: {datos['calificacion']}|")
        print()

def eliminar_estudiante():
    nombre = input("Nombre del estudiante a eliminar: ")
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"\nEstudiante {nombre} eliminado.\n")
    else:
        print("\nEstudiante no encontrado.\nIngrese una opcion nuevamente")

def menu():
    while True:
        print("Menú:\n 1. Agregar estudiante\n 2. Modificar calificación\n " \
        "3. Mostrar estudiantes\n 4. Eliminar estudiante\n 5. Salir")
        opcion = input("\nElige una opción: ")

        if opcion == '1':
            agregar_estudiante()
        elif opcion == '2':
            modificar_calificacion()
        elif opcion == '3':
            mostrar_estudiantes()
        elif opcion == '4':
            eliminar_estudiante()
        elif opcion == '5':
            print("\nSaliendo del programa.")
            break
        else:
            print("\nOpción no válida.\n")



# Ejecutar el menú
menu()
