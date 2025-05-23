#imprimir los numeros pares  del 1 al  20 
for i in range(0,21,2):
    print("\n",i)

print("_" *30)


#usando un condicional seria de esta forma
for numero in range(1, 21):
    if numero % 2 == 0:
        print("\n", numero)