"""
Escribe una función llamada es_mayor_de_edad(edad) que reciba
un entero y retorne "Mayor" si tiene 18 años o más, y "Menor"
en caso contrario
-prueba1:es_mayor_de_edad(17):"Menor"
-prueba2:es_mayor_de_edad(18):"Mayor"
-prueba3:es_mayor_de_edad(45):"Mayor"
"""
#verifica si una persona es mayor de edad
def es_mayor_de_edad(edad):
#si la edad es 18 o mas, es mayor de edad
	if edad>=18:
		return "Mayor"
#si es menos de 18, es menor de edad
	else:
		return "Menor"
#resultados
print(es_mayor_de_edad(17))
print(es_mayor_de_edad(18))
print(es_mayor_de_edad(45))