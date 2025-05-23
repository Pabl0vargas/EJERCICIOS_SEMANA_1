#Menú interactivo
opcion = ""
while opcion != "3":
    print("\nMenú:\n 1. Saludar\n 2. Despedirse\n 3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("¡Hola!")
    elif opcion == "2":
        print("¡Adiós!")
    elif opcion != "3":
        print("Opción no válida.")
print("Programa terminado.")
