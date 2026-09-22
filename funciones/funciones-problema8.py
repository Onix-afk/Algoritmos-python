"""
Diseña una función llamada area_triangulo(base,altura) que
calcule el área mediante la fórmula(baseXaltura)/2 y valide
que ambos valores sean mayores a cero;si no lo son, debe 
retornar 0.
-prueba1:area_triangulo(10,5):25.0
-prueba2:area_triangulo(7,4):14.0
-prueba3:area_triangulo(-2,5):0
"""
#calcula el area de un triangulo
def area_triangulo(base,altura):
#calcula si ambos valores son mayores a 0	
	if base>0 and altura>0:
		return (base*altura)/2
#si alguno no es valido, devuelve 0
	else:
		return 0
#resultados
print(area_triangulo(10,5))
print(area_triangulo(7,4))
print(area_triangulo(-2,5))