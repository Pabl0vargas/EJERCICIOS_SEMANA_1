contactos = {}

def agregar_contacto ():
    nombre = input("\nIngrese el nombre del contacto: ").lower()
    num_tel = int(input("\nIngrese el numero de telefono: "))
    contactos[nombre] = num_tel
    print(f"\ncontacto {nombre} agregado")
agregar_contacto()    

def lista_contactos():
    if not contactos:
        print("\nNo hay contactos")
    else:
        print("\nLista de contactos")
        for nom, telef in contactos.items():
            print(f"|contacto: {nom}| telefono: {telef}|")
        print()

def buscar_contacto():
    nombre = input("ingrese el nombre del contacto que va a buscar: ")
    if nombre in contactos:
        print(f"el contacto es {nombre} y el numero es : {contactos.get(nombre)} ")        
def menu():
    while True:
        print("MENU:\n 1. Agregar nuevo contacto\n 2. Mostrar todos los contactos\n" \
        "3. Buscar un contacto por su nombre\n ")
        opcion = input("Elige una opcion: ")

        if opcion == '1' :
            agregar_contacto()
        elif opcion == '2' :
            lista_contactos()
        elif opcion == '3' :
            buscar_contacto() 
    



menu()
