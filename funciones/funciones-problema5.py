"""
Escribe una función llamada longitud_nombre(nombre) que
reciba una cadena y retorne cuántas letras tiene usando len().
-prueba1:longitud_nombre("Lucia"):5
-prueba2:longitud_nombre("Sol"):3
-prueba3:longitud_nombre(""):0
"""
#recibe un texto y devuelve la cantidad de caracteres
def longitud_nombre(nombre):
	return len(nombre)
#resultados
print(longitud_nombre("Lucia"))
print(longitud_nombre("Sol"))
print(longitud_nombre(""))