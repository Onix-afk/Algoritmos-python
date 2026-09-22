"""
Diseña una función llamada mayor_de_tres(a,b,c) que reciba
tres números y determine cuál es el mayor utilizando únicamente
operadores lógicos(and) y comparaciones(>=),sin emplear
max().Por ejemplo:si a>=b y a>=c,el mayor es a.La función
debe devolver el número más grande encontrado.
-Prueba1:mayor_de_tres(5,12,9)
-Prueba2:mayor_de_tres(20,3,1)
-Prueba3:mayor_de_tres(4,4,4)
"""
#recibe tres números y devuelve el mayor
def mayor_de_tres(a,b,c):
#si a es mayor o igual que los otros dos
	if a>=b and a>=c:
		return a
#si b es mayor o igual a los otros dos
	elif b>=a and b>=c:
		return b
#si no se cumple nada de lo anterior, c es mayor
	else:
		return c
#se muestran los resultados
print(mayor_de_tres(5,12,9))
print(mayor_de_tres(20,3,1))
print(mayor_de_tres(4,4,4))