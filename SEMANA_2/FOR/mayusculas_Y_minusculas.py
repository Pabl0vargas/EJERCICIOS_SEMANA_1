# Pedir al usuario una palabra e imprimir cuantas may y min hay
palabra = input("Ingresa una palabra: ")

mayusculas = 0
minusculas = 0

for i in palabra:
    if i.isupper():
        mayusculas += 1
    elif i.islower():
        minusculas += 1
print("La cantidad de letras mayúsculas es: ", mayusculas)
print("La cantidad de letras minúsculas es: ", minusculas)  

mayusculas = 0
minusculas = 0

for letra in palabra:
    if 'A' <= letra <= 'Z':
        mayusculas += 1
    elif 'a' <= letra <= 'z':
        minusculas += 1        


print("La cantidad de letras mayúsculas es: ", mayusculas)
print("La cantidad de letras minúsculas es: ", minusculas)
