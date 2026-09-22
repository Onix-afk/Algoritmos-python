"""
Crea una función llamada calificar(nota) que reciba un 
número decimal o entero que represente una calificación
de 0 a 100.Utilizando una cadena de condiciones if/elif/else:
-si la nota es mayor o igual a 90,retorna "A".   
-si está entre 80 y 89 inclusive,retorna "B".   
-si está entre 70 y 79 inclusive,retorna "C".   
-si es menor estrictamente a 70,retorna "F".   
"""
#asigna una letra segun la calificación
def calificar(nota):
#si es igual o mayor de 90 es A
	if nota >= 90:
		return "A"
#si es mayor o igual a 80 es B
	elif nota >= 80:
		return "B"
#si es mayor o igual a 70 es C
	elif nota >=70:
		return "C"
#si es menos de 70 es F
	else:
		return "F"
#se pide la calificacion
nota=float(input("Ingresa la calificacion(0-100)"))
#se llama la funcion y se guarda el resultado
res=calificar(nota)
#se muestran los resultados
print(f"calificacion: {nota}")
print(f"{res}")
