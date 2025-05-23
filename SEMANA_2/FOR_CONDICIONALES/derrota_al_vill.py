print ("Escenario 1. Enfrentarse a un villano fuerte")
print(" ")

print("Bienvenido a your are the hero!..........")
print("")
print("""Estas avanzando en tu historia, por error caiste en puente dimensional que te llevo a la 
guarida secreta de un villano muy superior a tus habilidades, te llevara al limite y 
te matara incontables veces hasta que logres vencerlo.""")
print("")
print("<Tienes que seleccionar uno de los heroes para enfrentar esta batalla>")
print("1. FireBlast: elemento fuego")
print("2. LadyWater: elemento agua")
print("3. Terremoto: elemento tierra")
print("4. AirBender: elemento viento")
print("")
heroe = int(input("Escoge un heroe para pelear la batalla: "))
print("")

if heroe == 1:
    print("Has seleccionado al heroe FireBlast")
    print("")
    ataque = input("¿Deseas realizar el primer ataque?(si o no) ")
    if ataque == "si":
        print("Ataque realizado: triple patada de fuego volcanico")
        print("Has recibido un ataque de tierra interminable que extinguio tu fuego y te asesino")
    else:
        print("Has recibido un ataque de tierra interminable que extinguio tu fuego y te asesino")
    
    print("")
    print("<Para continuar batalla seleccionar otro herore>")
    print("2. LadyWater: elemento agua")
    print("3. Terremoto: elemento tierra")
    print("4. AirBender: elemento viento")
    print("")
    heroe = int(input("Escoge un heroe para pelear la batalla: "))
    print("")
    if heroe == 2:
        print("Has seleccionado a la heroina LadyWater")
    elif heroe == 3:
        print("Has seleccionado al heroe Terremoto")

    elif heroe == 4:
        print("Has seleccionado al heroe AirBender")

    print("Tu villano utilizo gran parte de su enegia en el anterior ataque y quedo debil")
    print("Tu heroe utilizo su poder secreto")
    print("Tu heroe logro vencer al villano felicidades") 
elif heroe == 2: 
    print("Has seleccionado a la heroina LadyWater")
    print("")
    ataque = input("¿Deseas realizar el primer ataque?(si o no) ")
    if ataque == "si":
        print("Ataque realizado: Cañon de agua con veneno")
        print("Has recibido un ataque de fuego que evaporo tu agua y has muerto")
    else:
        print("Has recibido un ataque de fuego que evaporo tu agua y has muerto")
    
    print("")
    print("<Para continuar batalla seleccionar otro herore>")
    print("1. FireBlast: elemento fuego")
    print("3. Terremoto: elemento tierra")
    print("4. AirBender: elemento viento")
    print("")
    heroe = int(input("Escoge un heroe para pelear la batalla: "))
    print("")
    if heroe == 1:
        print("Has seleccionado al heroe FireBlast")
    elif heroe == 3:
        print("Has seleccionado al heroe Terremoto")
    elif heroe == 4:
        print("Has seleccionado al heroe AirBender")
    print("")
    print("Tu villano utilizo gran parte de su enegia en el anterior ataque y quedo debil")
    print("Tu heroe utilizo su poder secreto")
    print("Tu heroe logro vencer al villano felicidades") 
elif heroe == 3: 
    print("Has seleccionado al heroe Terremoto")
    print("")
    ataque = input("¿Deseas realizar el primer ataque?(si o no) ")
    if ataque == "si":
        print("Ataque realizado: Lluvia de rocas")
        print("Has recibido un tsunami de agua y has muerto")

    else:
        print("Has recibido un tsunami de agua y has muerto")
    
    print("")
    print("<Para continuar batalla seleccionar otro herore>")
    print("1. FireBlast: elemento fuego")
    print("2. LadyWater: elemento agua")
    print("4. AirBender: elemento viento")
    print("")
    heroe = int(input("Escoge un heroe para pelear la batalla: "))
    print("")
    if heroe == 1:
        print("Has seleccionado al heroe FireBlast")
        print("")
    elif heroe == 2:
        print("Has seleccionado al heroe LadyWater")
        print("")
    elif heroe == 4:
        print("Has seleccionado al heroe AirBender")
        print("")
    print("Tu villano utilizo gran parte de su enegia en el anterior ataque y quedo debil")
    print("Tu heroe utilizo su poder secreto")
    print("Tu heroe logro vencer al villano felicidades") 
elif heroe == 4: 
    print("Has seleccionado al heroe AirBender")
    print("")
    ataque = input("¿Deseas realizar el primer ataque?(si o no) ")
    if ataque == "si":
        print("Ataque realizado: vendabal de aire cortante")
        print("Has recibido un ataque de hielo superior que te congelo hasta morir")

    else:
        print("Has recibido un ataque de hielo superior que te congelo hasta morir")
        
    print("")
    print("<Para continuar batalla seleccionar otro herore>")
    print("1. FireBlast: elemento fuego")
    print("2. LadyWater: elemento agua")
    print("3. Terremoto: elemento tierra")
    print("")
    heroe = int(input("Escoge un heroe para pelear la batalla: "))
    print("")
    if heroe == 2:
        print("Has seleccionado a la heroina LadyWater")
    elif heroe == 3:
        print("Has seleccionado al heroe Terremoto")
    elif heroe == 1:
        print("Has seleccionado al heroe FireBlast")

    print("Tu villano utilizo gran parte de su enegia en el anterior ataque y quedo debil")
    print("Tu heroe utilizo su poder secreto")
    print("Tu heroe logro vencer al villano felicidades") 
else:
    print("Opcion incorrecta.")