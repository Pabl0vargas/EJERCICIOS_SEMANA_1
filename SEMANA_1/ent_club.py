#sistema de control de acceso a un club
pase = "si" or "no" 
edad = int(input("ingrese su edad "))
#validacion de edad
if edad < 18 :
    print(" no puede entrar al club ")
#validacion de pase
else:
   pase=input("¿tienes pase dorado?, ingrese si o no ").lower()

if pase == "si" and edad >=18:
       print("puede entrar al club")
elif pase == "no" and edad >=18 and edad <=25:
          print ("puede ingresar al club")
elif edad > 25 and pase == "no":        
    print("no puede ingresar al club")
       
      
   
   
       
       
       




    