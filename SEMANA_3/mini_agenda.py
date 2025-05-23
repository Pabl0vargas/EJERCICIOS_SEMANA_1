# Lista para almacenar contactos (cada uno es un diccionario)
agenda = []

# Agregar un nuevo contacto
def agregar_contacto(nombre, celular, estado_civil, genero):
    contacto = {
        "nombre": nombre,
        "celular": celular,
        "estado_civil": estado_civil,
        "genero": genero
    }

    agenda.append(contacto)
   

# Mostrar todos los contactos
def mostrar_contactos():
    if not agenda:
        print("\n No hay contactos en la agenda.\n")
    else:
        print("\n Contactos registrados:")
        for i, contacto in enumerate(agenda):
            print(f"{i + 1}. |Nombre: {contacto['nombre']}| Celular: {contacto['celular']}| "
                  f"Estado Civil: {contacto['estado_civil']}| Género: {contacto['genero']}")
        print()


# Buscar un contacto por nombre o celular
def buscar_contacto(nombre):
    
    for contacto in agenda:
        if contacto["nombre"] == nombre or contacto["celular"] == nombre:
            return contacto
    return None

    

# Modificar un contacto
def modificar_contacto(nombre, new_nombre=None, new_celular=None, new_estado_civil=None, new_genero=None):
    contacto = buscar_contacto(nombre)
    if contacto:
        if new_nombre:
            contacto["nombre"] = new_nombre
        if new_celular:
            contacto["celular"] = new_celular
        if new_estado_civil:
            contacto["estado_civil"] = new_estado_civil
        if new_genero:
            contacto["genero"] = new_genero
        return True
    return False

# Eliminar un contacto
def eliminar_contacto(nombre):
    for contacto in agenda:
        if contacto["nombre"] == nombre:
            agenda.remove(contacto)
            return True
    return False

# Menú principal
def menu():
     print("=======  AGENDA DE CONTACTOS =======")
     print("\n 1. Agregar contacto\n 2. Buscar contacto\n 3. Mostrar todos los contactos\n" \
    " 4. Modificar contacto\n 5. Eliminar contacto\n 6. Salir")
while True:
    menu()
    opcion = input(" Elige una opción: ")
    match opcion:
        case "1":
            print("\n Agregar nuevo contacto:")
            nombre = input("Nombre: ")
            celular = input("Celular: ")
            estado_civil = input("Estado civil: ")
            genero = input("Género: ")
            agregar_contacto(nombre, celular, estado_civil, genero)
            print(f" Contacto {nombre} agregado correctamente.\n")
        case '2':
            nombre = input("\n Buscar por nombre o celular: ").lower()
            contacto = buscar_contacto(nombre)  
            if contacto:
                print(f"\n| Nombre: {contacto['nombre']}| celular: {contacto['celular']}| Estado civil: {contacto['estado_civil']}| Genero: {contacto['genero']}")
            else:
                print("Contacto no encontrado.")
            
        case '3':
            mostrar_contactos()
        case '4':
            criterio = input("Ingrese el nombre del contacto a modificar: ")
            new_nombre = input("Ingrese el nuevo nombre (si se deja vacio, no se modifica): ")
            new_celular = input("Ingrese el nuevo celular (si se deja vacio, no se modifica): ")
            new_estado_civil = input("Ingrese el nuevo estado civil (si se deja vacio, no se modifica): ")
            new_genero = input("Ingrese el nuevo genero (si se deja vacio, no se modifica): ")
            if modificar_contacto(nombre, new_nombre, new_celular, new_estado_civil, new_genero):
                print(f"Contacto {nombre} modificado con éxito.")
            else:
                print("Contacto no encontrado.")

        case '5':
            mostrar_contactos()
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            if eliminar_contacto(nombre):
                print(f"Contacto {nombre} eliminado con éxito.")
            else:
                print("Contacto no encontrado.")
        case '6':
            print(" Saliendo de la agenda. ¡Hasta pronto!")
            break 
        case _:
            print(" Opción inválida. Intenta de nuevo.\n")

# Ejecutar el programa
