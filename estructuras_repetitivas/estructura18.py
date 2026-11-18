"""
Análisis de velocidad de vehículo (Multas y promedios): Un radar registra la 
velocidad de 12 vehículos en una carretera donde el límite es 90 km/h. Cuenta 
cuántos vehículos iban dentro del límite y cuántos cometieron infracción. De los 
infractores, indica cuántos superaban los 110 km/h (multa grave).
"""
#se declara el limite como 90 y la multa como 110
limite=90
multa=110
#Se crean acumuladores 
infracciones=0
dentro=0
sobre_limite=0
#se solicita la velocidad de 12 vehiculos en un ciclo de 12 vueltas
print("Ingrese las velocidades de los 12 vehiculos: ")
for i in range(1, 13):
	velocidad=float(input(f"Vehiculo {i}: "))
#si la velocidad es menor a 91, se incrementa el contador de dentro del limite
	if velocidad<=limite:
		dentro+=1
#si la velocidad es menor a 111, se incrementa el contador de infracciones
	elif  velocidad<=multa:
		infracciones+=1
#si la velocidad es mayor a 110, se incrementa el contadoe de sobre_limite
	else:
		sobre_limite+=1
#se muestran los resultados de cada categoria
print(f"Total de vehiculos que cometieron infracción: {infracciones}")
print(f"vehiculos con multa grave(>110km/h): {sobre_limite}")
print(f"vehiculos dentro del limite: {dentro}")
