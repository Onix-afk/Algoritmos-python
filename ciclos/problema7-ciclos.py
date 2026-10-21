"""
Un sensor en la puerta de una discoteca registra la edad de 8
personas que intentan entrar. Usa un contador para determinar
cuántas personas son menores de edad(menores a 18 años).
"""
#se crea el contador de menores en 0
menor=0
#se crea un ciclo que de 8 vueltas
for i in range(8):
#se hace un input que pida la edad por cada vuelta del ciclo
	edad=int(input(f"Ingresa la edad de la persona{i+1}: "))
#se verifica si la edad ingresada es menor de 18
	if edad<18:
#se suma el menor al contador
		menor+=1
#se muestra la cantidad de menores
print(f"Cantidad de menores de edad: {menor}")