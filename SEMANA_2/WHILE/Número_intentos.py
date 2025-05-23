#Número de intentos
numero = int(input("Ingresa un número entre 1 y 10: "))

while numero < 1 or numero > 10:
    numero = int(input("Número inválido. Intenta de nuevo (1-10): "))

print("Número válido:", numero)
