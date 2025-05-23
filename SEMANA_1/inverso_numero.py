#Inverso de número de tres cifras
numero_str = input("digite 3 numeros " )
#inversion del numero
numero_inverso = numero_str[::-1]

numero_int = int(numero_str)
# Validar que el número ingresado sea de tres cifras
if numero_int > 999: 
    print("error, numero maximo excedido")
    #operaciones para extraer las cifras
else:
    centena = numero_int // 100
    decena = (numero_int % 100) // 10
    unidad = numero_int % 10
    #resultados
    print("centena: ", centena)
    print("decena: ", decena)
    print("unidad: ", unidad)
    print("el numero original es :",numero_int)
print("\n el numero inverso es :",numero_inverso)  




