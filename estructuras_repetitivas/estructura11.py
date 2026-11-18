"""
 Estadística de edades por rangos: En una encuesta aplicada a  personas, se 
registra la edad de cada participante. Clasifica y cuenta cuántas personas son niños 
(0-12 años), adolescentes (13-17 años), adultos (18-59 años) y adultos mayores (60 
años o más). 
"""
#se pide la cantidad de personas encuestadas
N=int(input("Número de personas encuestadas: "))
#se crena acumuladores para niños,adolescentes,adultos y adultos mayores
niños=0
adolescentes=0
adultos=0
adultos_mayores=0
#se crea un ciclo que de vueltas por cada persona encuestada
for i in range(N):
#se pide la edad de la persona en cada vuelta
	edad=int(input(f"Ingresa la edad de la persona {i+1}: "))
#si edad es menor o igual a 12 se suma 1 a niños 
	if edad<=12:
		niños+=1
#si edad es menor a 17 y mayor a 12 se suma 1 a adolescentes 
	elif edad<=17:
		adolescentes+=1
#si edad es menor a 59 y mayor a 17 se suma 1 a adultos 
	elif edad<=59:
		adultos+=1
#si edad es mayor a 59 se suma 1 a adultos mayores
	else:
		adultos_mayores+=1
#se muestra la cantidad de encuestados de cada categoria de edad
print(f"Niños(0-12): {niños}")
print(f"Adolescentes(13-17): {adolescentes}")
print(f"Adultos(18-59): {adultos}")
print(f"Adultos Mayores(60+): {adultos_mayores}")