"""
Revisa en un ciclo el peso registrado de 10 maletas y 
cuenta cuántas superan el límite de 23kg
"""
#se declaran 10 pesos diferentes en una lista
pesos_maletas=[23,24,15,16,18,40,12,13,19,20]
#se crea un contador
contador=0
#se crea un ciclo de 10 vueltas
for i in range(10):
#para que imprima cada elemento de la lista
	print(pesos_maletas[i])
#se verifica si el peso es mayor a 23 y los mayores se suman al contador
	if(pesos_maletas[i]>23):
		contador+=1
#se muestra si el peso verificado es mayor a 23kg
		print(f"La maleta de peso {pesos_maletas[i]} es mayor a 23 kilos")
#se muestra el total de maletas que pesan mas de 23kg
print(f"El total de maletas mayor a 23kg es {contador}")