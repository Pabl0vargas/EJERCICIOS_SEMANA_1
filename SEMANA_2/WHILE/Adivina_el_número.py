#Adivina el número
secreto = 7
intento = int(input("Adivina el número (entre 1 y 10): "))

while intento != secreto:
    if intento < secreto:
        print("Demasiado bajo.")
    else:
        print("Demasiado alto.")
    intento = int(input("Intenta de nuevo: "))

print("¡Correcto!")
