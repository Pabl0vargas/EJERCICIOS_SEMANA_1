#veterinaria
# Listas para almacenar la información de los animales
nombres = []
edades = []
estado_salud = []

# Función para agregar un animal
def agregar_animal():
    nombre = input("Nombre del animal: ").strip()
    edad = input("Edad del animal: ").strip()
    enfermo = input("¿Está enfermo? (sí/no): ").strip().lower()

    nombres.append(nombre)
    edades.append(edad)
    estado_salud.append("Enfermo" if enfermo == "sí" else "Sano")

    print(f"Animal '{nombre}' agregado correctamente.")

# Función para eliminar un animal por nombre
def eliminar_animal():
    nombre = input("Nombre del animal a eliminar: ").strip()
    if nombre in nombres:
        index = nombres.index(nombre)
        nombres.pop(index)
        edades.pop(index)
        estado_salud.pop(index)
        print(f"Animal '{nombre}' eliminado correctamente.")
    else:
        print(f"No se encontró un animal con el nombre '{nombre}'.")

# Función para listar todos los animales registrados
def listar_animales():
    if not nombres:
        print("No hay animales registrados.")
    else:
        print("\nLista de animales registrados:")
        for i in range(len(nombres)):
            print(f"{i+1}. Nombre: {nombres[i]}, Edad: {edades[i]}, Estado de salud: {estado_salud[i]}")

# Menú principal
def menu():
    while True:
        print("\n--- Menú de Gestión de Animales ---")
        print("1. Agregar un animal")
        print("2. Eliminar un animal por nombre")
        print("3. Listar todos los animales registrados")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_animal()
        elif opcion == "2":
            eliminar_animal()
        elif opcion == "3":
            listar_animales()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
menu()
