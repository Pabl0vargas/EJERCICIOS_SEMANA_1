#juego de FizzBuzz
numero = int(input("ingrese un numero "))
#operador modulo para los multiplos
multiplo3 = numero%3
multiplo5 = numero%5
#validar si el numero es multiplo de 3 o 5

if (multiplo3 ==0 and multiplo5 ==0 ) :
    print("FizzBuzz")
elif(multiplo5 ==0 ) :
    print("BUZZ")  
elif(multiplo3 == 0) :
  print("FIZZ")
else:  print(numero)
