"""
Implementa una función llamada operacion_basica(a,b,operacion)
donde a y b son operandos númericos y operacion es una cadena.
Usa ramas condicionales para comparar el texto:si vale "suma", 
devuelve a+b;si vale "resta" devuelve a-b;si vale "multiplica",
devuelve a x b.Si el texto recibido no coincide con ninguna de 
esas opciones, debe retornar "Operación no válida".
-Prueba1:operacion_basica(6,4,"resta"):2 
-Prueba2:operacion_basica(5,3,"multiplica"):15 
-Prueba3:operacion_basica(10,2,"raíz"):"Operación no válida" 
"""
#realiza una operación entre dos números según lo indicado
def operacion_basica(a,b,operacion):
#verifica si es suma y devuelve el resultado
	if operacion=="suma":
		return a+b
#verifica si es resta y devuelve el resultado
	elif operacion=="resta":
		return a-b
#verifica si es multiplicacion y devuelve el resultado
	elif operacion=="multiplica":
		return a*b
#verifica si es division y devuelve el resultado
	elif operacion=="division":
		return a/b
#si la opcion no coincide se muestra un mensaje
	else:
		return "operacion no valida"
#Se muestran los resultados
print(operacion_basica(6,4,"resta"))
print(operacion_basica(5,3,"multiplica"))
print(operacion_basica(10,2,"raiz"))