"""
Crea una función llamada obtener_signo(numero) que reciba un
número real o entero.Mediante las ramas if,elif y else,clasifica
el valor:retorna "Positivo" si es mayor que cero, "Negativo" si es 
menor que cero, o "Cero" si es exactamente igual a cero.
-Prueba1:obtener_signo(12):"Positivo"
-Prueba2:obtener_signo(-8):"Negativo"
-Prueba3:obtener_signo(0):"Cero"
"""
#indica si un numero es positivo, negativo o cero
def obtener_signo(numero):
#si es mayor a 0 es positivo
	if numero > 0:
		return "Positivo"
#si es menor a 0 es negativo
   elif numero < 0:
      return "Negativo"
#si no se cumple lo anterior es cero
	else:
   	return "Cero"
#pruebas
print(obtener_signo(12))
print(obtener_signo(-8))
print(obtener_signo(0))