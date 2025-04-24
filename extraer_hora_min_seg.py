#convertir segundos a horas, minutos y segundos
# Definicion de variables
segundos = int(input(" ingrese la cantidad de segundos a convertir: "))
# Calculo de horas, minutos y segundos
horas = segundos // 3600
modulohoras = segundos % 3600
minutos = modulohoras // 60 
segundoss = modulohoras % 60
# Imprimir resultado
print ("Horas : ", horas, "minutos: ", minutos, "segundos: ", segundoss)

