# Contraseña correcta
contraseña_correcta = "python123"

intentos_totales = 3

for intento in range(intentos_totales):
    contraseña = input("Ingresa la contraseña: ")
    
    if contraseña == contraseña_correcta:
        print("Acceso permitido")
        break  # salir del ciclo si la contraseña es correcta
    else:
        intentos_restantes = intentos_totales - (intento + 1)
        if intentos_restantes > 0:
            print(f"Contraseña incorrecta. Te quedan {intentos_restantes} intento(s).")
        else:
            print("Contraseña incorrecta.")


else:
    print("Acceso denegado. Has agotado tus intentos.")