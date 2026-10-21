"""
Revisa la entrada de peso de 10 maletas en un ciclo y cuenta
cuántas superan el límite de 23kg
"""
#se crea un contador en 0
contador=0
#se hace un ciclo de 10 vueltas
for i in range(10):
#se pide el peso de la maleta por cada vuelta
	pesos_maletas=float(input(f"Ingresa el peso de la maleta{i+1}: "))
#se muestra el peso ingresado
	print(pesos_maletas[i])
#se verifica si el peso es mayor a 23kg, y si es mayor se suma al contador
	if(pesos_maletas >23):
		contador+=1
#se muestra el total de maletas que pesan mas de 23kg
print(f"El total de maletas mayor a 23k es {contador}")