#taller arrays

mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ,14 ,15]

lista_vacia_1 = []

lista_nombres = ["Juan", "Maria", "Pedro"]

mi_lista[0] #accedemos al primer elemento

#indice negativo
mi_lista[-1]  # Último elemento
mi_lista[-2]  # Penúltimo

#si sintento acceder a un indice que no existe el sistema nos arroja error

print(mi_lista[10])  # Error: IndexError

#imprimir el primer y ultimo valor
lista2 = [10, 20, 30, 40]
print(lista2[0])
print(lista2[3])


#sublista usando slicing
mi_lista = [0, 1, 2, 3, 4, 5]
sublista = mi_lista[1:4]  # Resultado: [1, 2, 3]

#modificar los elementos de una lista
mi_lista[2] = 100

#agregar nuevos elementos a una lista
mi_lista.append(99)

#inserta un elemento en una posición específica
mi_lista.insert(2, "nuevo")

#combinar dos listas en una sola
lista1 = [1, 2]
lista2 = [3, 4]
combinada = lista1 + lista2

#elimina un valor específico de una lista
mi_lista.remove(20)  # Elimina el primer 20 que encuentre
#usando el metodo pop()
mi_lista.pop()      # Último
mi_lista.pop(1)     # Índice específico
#usando el metodo del
del mi_lista[1]  # Elimina el segundo elemento


#verifica si un elemento está presente
if 10 in mi_lista:
    print("Está presente")

#encontrar el índice de un elemento
mi_lista.index(10)  # Devuelve el primer índice donde está 10

#contar cuántas veces aparece un valor
mi_lista.count(10)

#ordena una lista de manera ascendente
mi_lista.sort()

#ordena en orden descendente
mi_lista.sort(reverse=True) 
#sort() modifica la lista original.
#sorted() devuelve una nueva lista ordenada.

#para hacer una copia de una lista se puede usar
#slicing
copia = mi_lista[:]
#list()
copia = list(mi_lista)
#copy()
copia = mi_lista.copy()

#comprobamos si una lista está vacía
if not mi_lista:
    print("La lista está vacía")


#pedimos al usuario la cantidad de datos
n = int(input("¿Cuántos datos quieres ingresar? "))
#almacenamos esos datos en una lista usando for
datos = []

for i in range(n):
    valor = input(f"Ingrese el dato #{i + 1}: ")
    datos.append(valor)
