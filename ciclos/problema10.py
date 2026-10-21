"""
Revisa en un ciclo el peso registrado de 10 maletas 
y cuenta cuántas superan el límite de 23kg
"""
#se declaran las edades de 10 dentro de una lista
edades=[32,18,17,13,21,5,10,40]
#se crea un contador para los menores
menor=0
#se crea un ciclo de 8 vueltas
for i in range(8):
#se imprime la edad
	print(edades[i])
#se verifica si la edad es menor a 18
	if edades[i]<18:
#si es menor se suma al contador		
		menor+=1
#se imprime el total de menores
print(f"Cantidad de menores de edad: {menor}")