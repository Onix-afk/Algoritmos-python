"""
Realice un algoritmo para generar e imprimir los números
pares que se encuentran entre 0 y 100
"""
#se crea un contador para los números impares
impar=0
#se crea un contador para los números pares
par=0
#se crea un ciclo que inicia en 1 y termina en 100
for i in range(1,100):
#se verifica si el numero es par y se guarda en su contador especifico
	if i%2==0:
		par+=1
	else:
		impar+=1
#se muestra el total de numeros pares
print(f"pares: {par}")
#se muestra el total de numeros impares
print(f"impares: {impar}")