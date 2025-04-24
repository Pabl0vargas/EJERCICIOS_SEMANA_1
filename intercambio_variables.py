# Intercambio de variables
num1 = int(input("ingrese el primer valor " ))
num2 = int(input("ingrese el segundo valor " ))
#imprimir los valores antes del intercambio
print("\nAntes del intercambio:")

print("su valor 1 es: ", num1)
print("su valor 2 es: ", num2)

print("\nDespués del intercambio:")
#intercambiar los valores
num1, num2 = num2, num1
#imprimir los valores después del intercambio
print("su valor 1 es : ", num1)
print("su valor 2 es : ", num2)
