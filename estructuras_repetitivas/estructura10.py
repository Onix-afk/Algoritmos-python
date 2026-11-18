"""
Evaluación de grupo académico (Aprobados, Reprobados y Excelencia): Lee las 
calificaciones finales de  estudiantes de un curso. Clasifícalos en tres categorías: 
Reprobados (<6.0), Aprobados ( 6.0 a 9.0 ) y Excelencia ( 9.0 a 10.0 ).Muestra la
cantidad de alumnos por categoría y el promedio general del grupo. 
"""
#se pide la cantidad de estudiantes
N=int(input("Número de estudiantes: "))
#se crean acumuladores para los aprobados,reprobados y con excelencia
aprobados=0
reprobados=0
excelencia=0
#se crea un ciclo que de vueltas por cada estudiante 
for i in range(N):
#se pide la calificacion al estudiante en cada vuelta
	calif=float(input(f"Calificación del estudiante{i+1}: "))
#si la calificacion es mayor 0 igual 9.0 se suma 1 a excelencia
	if calif>=9.0:
		excelencia+=1
#si la calificacion es mayor o igual a 6.0 pero menor a 9.0 se suma 1 a aprobados
	elif calif>=6.0:
		aprobados+=1
#si es menor a 6.0 se suma uno a reprobados
	else:
		reprobados+=1
#se muestra la cantidad de aprobados,reprobados y con excelencia
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")
print(f"Excelencia: {excelencia}")