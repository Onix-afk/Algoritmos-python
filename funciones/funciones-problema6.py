"""
Crea una función llamada mayor_de_dos(a,b) que devuelve el
número más grande sin usar la función integrada max().Si son
iguales, retorna cualquiera de dos.
-Prueba1:mayor_de_dos(15,27):27
-Prueba2:mayor_de_dos(40,-10):40
-Prueba3:mayor_de_dos(8,8):8
"""
#compara 2 números y devuelve el mayor
def mayor_de_dos(a,b):
#si a es mayor que b devuelve a
	if a>b:
		return a
#si no, devuelve b
	else:
	   return b
#resultados
print(mayor_de_dos(15,27))
print(mayor_de_dos(40,-10))
print(mayor_de_dos(8,8))	