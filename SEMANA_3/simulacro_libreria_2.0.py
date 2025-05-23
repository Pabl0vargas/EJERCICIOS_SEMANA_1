# Lista de géneros permitidos
GENRES = ["Fiction", "NonFiction", "Science", "Biography", "Children"]

# Diccionario que almacena los libros
biblioteca = {}

# Añadir un libro
def agregar_libro():
    if len(biblioteca) >= 10:
        print("Ya hay 10 o más libros en la biblioteca.")
    titulo = input("Título del libro: ").strip()
    if titulo in biblioteca:
        print("Este libro ya existe en la biblioteca.")
        return

    autor = input("Autor del libro: ").strip()
    while True:
        cantidad = input("Cantidad de copias disponibles: ")
        if cantidad.isdigit() and int(cantidad) > 0:
            cantidad = int(cantidad)
            break
        else:
            print("Por favor, introduce un número válido mayor que 0.")

    while True:
        genero = input("Género del libro (Fiction, NonFiction, Science, Biography, Children): ").strip()
        if genero in GENRES:
            break
        else:
            print("Género inválido. Intenta nuevamente.")

    biblioteca[titulo] = {
        "autor": autor,
        "copias_disponibles": cantidad,
        "copias_originales": cantidad,
        "genero": genero
    }
    print(f"Libro '{titulo}' agregado con éxito.")

# Buscar un libro por título
def buscar_libro():
    titulo = input("Ingresa el título del libro a buscar: ").strip()
    libro = biblioteca.get(titulo)
    if libro:
        print(f"Título: {titulo}")
        print(f"Autor: {libro['autor']}")
        print(f"Copias disponibles: {libro['copias_disponibles']}")
        print(f"Género: {libro['genero']}")
    else:
        print("Book not found.")

# Registrar un préstamo
def prestar_libro():
    titulo = input("Ingresa el título del libro a prestar: ").strip()
    if titulo in biblioteca:
        if biblioteca[titulo]["copias_disponibles"] > 0:
            biblioteca[titulo]["copias_disponibles"] -= 1
            print("Préstamo registrado con éxito.")
        else:
            print("No hay copias disponibles para préstamo.")
    else:
        print("Book not found.")

# Registrar devolución
def devolver_libro():
    titulo = input("Ingresa el título del libro a devolver: ").strip()
    if titulo in biblioteca:
        if biblioteca[titulo]["copias_disponibles"] < biblioteca[titulo]["copias_originales"]:
            biblioteca[titulo]["copias_disponibles"] += 1
            print("Devolución registrada con éxito.")
        else:
            print("Todas las copias ya están disponibles.")
    else:
        print("Book not found.")

# Eliminar un libro
def eliminar_libro():
    titulo = input("Ingresa el título del libro a eliminar: ").strip()
    if titulo in biblioteca:
        if biblioteca[titulo]["copias_disponibles"] == biblioteca[titulo]["copias_originales"]:
            del biblioteca[titulo]
            print("Libro eliminado del catálogo.")
        else:
            print("No se puede eliminar: hay copias prestadas.")
    else:
        print("Book not found.")

# Listar libros por género
def listar_por_genero():
    genero = input("Ingresa el género (Fiction, NonFiction, Science, Biography, Children): ").strip()
    if genero not in GENRES:
        print("Género inválido.")
        return
    encontrados = [titulo for titulo, datos in biblioteca.items() if datos["genero"] == genero]
    if encontrados:
        print(f"Libros en el género '{genero}':")
        for titulo in encontrados:
            print(f"- {titulo} ({biblioteca[titulo]['copias_disponibles']} disponibles)")
    else:
        print("No hay libros disponibles de ese género.")

# Mostrar resumen de inventario
def mostrar_resumen():
    total_libros = len(biblioteca)
    total_copias = sum(libro["copias_disponibles"] for libro in biblioteca.values())
    print("\n=== Resumen de Inventario ===")
    print(f"Total de títulos en la biblioteca: {total_libros}")
    print(f"Total de copias disponibles: {total_copias}")
    print("=============================\n")

# Menú principal
def menu():
    while True:
        print("\n=== Biblioteca Comunitaria ===")
        print("1. Añadir libro")
        print("2. Buscar libro por título")
        print("3. Registrar préstamo")
        print("4. Registrar devolución")
        print("5. Eliminar libro del catálogo")
        print("6. Listar libros por género")
        print("7. Mostrar resumen de inventario")
        print("8. Salir")

        opcion = input("Selecciona una opción (1-8): ")
        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            buscar_libro()
        elif opcion == "3":
            prestar_libro()
        elif opcion == "4":
            devolver_libro()
        elif opcion == "5":
            eliminar_libro()
        elif opcion == "6":
            listar_por_genero()
        elif opcion == "7":
            mostrar_resumen()
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar el sistema
menu()
