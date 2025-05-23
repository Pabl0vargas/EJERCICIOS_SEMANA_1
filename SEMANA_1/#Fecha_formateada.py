#Fecha formateada
#revisar si las fechas son válidas
dia = int(input("Introduce el día: "))
if dia  >= 1 or dia <= 31:
        mes = int(input("Introduce el mes: "))
        if mes >= 1 or mes <= 12:
            año = int(input("Introduce el año: "))
            if año < 0:
                print("Año no válido")  
        else:
            print("Mes no válido")
else:
        print("Día no válido")

#formatear la fecha
DDMMAAAA = (f"{dia}/{mes}/{año}")
AAAAAMMDD = (f"{año}-{mes}-{dia}")
print("La fecha en formato DDMMAAAA es: ", DDMMAAAA)
print("La fecha en formato AAAAAMMDD es: ", AAAAAMMDD)

    