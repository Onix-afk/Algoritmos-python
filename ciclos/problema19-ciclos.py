"""
Un profesor tiene un salario inicial de $1500, y recibe un incremento de 10%
anual durante 6 años. ¿Cuál es su salario al cabo de 6 años? ¿Qué salario ha 
recibido en cada uno de los 6 años? Realice el algoritmo
"""
#se declara el salario en 1500
salario=1500
#se crea un ciclo de 6 vueltas
for año in range(6):
#se incrementa 10% al salario en cada vuelta
	salario=salario*1.10
#se muestra el año y el salario de ese año
	print(f"año{año} | salario:{salario}")
#se muestra el salario dentro de 6 años
print(f"en 6 años su salario sera: {salario}")