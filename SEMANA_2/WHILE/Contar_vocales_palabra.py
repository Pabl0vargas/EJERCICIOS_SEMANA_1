#Contar vocales en una palabra
palabra = input("Ingresa una palabra: ").lower()
i = 0
vocales = 0

while i < len(palabra):
    if palabra[i] in "aeiou":
        vocales += 1
    i += 1

print("Número de vocales:", vocales)
