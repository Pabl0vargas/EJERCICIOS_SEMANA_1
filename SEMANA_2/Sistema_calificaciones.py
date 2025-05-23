#Ingresamos la primera calificacion para ver si aprueba o no
calificacion1 = float(input("Ingrese una calificación numérica de 0 a 100: "))
if calificacion1 >= 60:
    print("Aprueba")
else:
    print("Desaprueba")

#Ingresamos una lista de calificaciones
while True:
    cal_ingresadas = input("\nIngresa las calificaciones separadas por comas (ej: 3.0,4.0,5.0): ")
    cal_separadas = cal_ingresadas.split(',') #usamos split para dividir un string en partes más pequeñas

    suma = 0 #Acumula la suma de todas las calificaciones válidas.
    cantidad = 0 #Cuenta cuántas calificaciones válidas hay
    lista_calificaciones = [] #lista vacia para agregar las calificaciones ingresadas

    #try_except para validar si el numero ingresado es valido o no
    for cs in cal_separadas:
        try:
            numero_convertido = float(cs.strip())#.strip() elimina espacios alrededor, por si el usuario puso " 4.5 " en lugar de "4.5".
            #float convierte los strings en decimales
            lista_calificaciones.append(numero_convertido)#agrega las notas a la lista vacia 
            suma += numero_convertido
            cantidad += 1
        except ValueError:
            print(f"'{cs}' no es un número válido ")
    #Calculamos el promedio
    if cantidad > 0:
        promedio = suma / cantidad
        print("\nEl promedio de las calificaciones es: {:.2f}".format(promedio))#usamos format para mostrar
        #el promedio con dos decimales
        break
    else:
        print("No se ingresaron calificaciones correctas.Intenta nuevamente: ") 
    

#Buscamos una calificación específica y la contamos
while True:# Repetir hasta que se ingrese un número decimal válido
    entrada = input("\n¿Qué calificación quiere buscar?: ")
    try:
        buscador_cal = float(entrada)
        break  # Salimos del ciclo si la conversión fue exitosa
    except ValueError:
        print(f"'{entrada}' no es una calificación válida. Intenta de nuevo.")



contador = 0
for n in lista_calificaciones:
    if n == buscador_cal:#comparador para ver si la cal ingresada se encuentra en la lista
        contador += 1 #si la encuentra la empieza a contar
    elif n < 0:
        continue 

if contador > 0:
    print("La calificación",buscador_cal, "aparece", contador, "vece(s)" )
else:
    print(f"La calificación {buscador_cal} no fue encontrada.")

#Contar cuántas calificaciones son mayores a la buscada
i = 0
mayores = 0

while i < len(lista_calificaciones):
    if lista_calificaciones[i] > buscador_cal:
        mayores += 1
    i += 1
    

print(f"\nHay {mayores} calificaciones mayores que {buscador_cal}.")