#contar cuántas veces aparece la letra "a" en una palabra ingresada
palabra = input("Ingrese una palabra: ")
contador = 0

for letra in palabra:
    if letra == "a":
        contador += 1

print("La letra 'a' aparece", contador, "veces en la palabra: ", palabra)