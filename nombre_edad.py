#validacion de datos(nombre, edad)
nombre = input("cual es tu nombre? ")

edad = int(input("cuantos años tines ? "))
 #validacion de edad
es_mayor = edad >= 18 
#resultado
print("hola, ", nombre)
print("eres mayor de edad? ", es_mayor)
print("tipo de dato de 'edad' : ", type(edad))
