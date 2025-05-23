#Sumar hasta detenerse
suma = 0
numero = int(input("Ingresa un número (0 para detenerse): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingresa otro número (0 para detenerse): "))

print("Suma total:", suma)
