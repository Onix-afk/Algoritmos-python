"""
Crea un programa que recorra los números del 1 al 20 e imprima
únicamente aquellos que sean pares, indicado al final cuántos
números pares se encontraron en total
"""
#se crea la variable contador que inicia en 0
contador=0
#se crea un for que da 20 vueltas e inicia en 1
for i in range(1,21):
#verificamos si el número es par 
	if i%2==0:
		print(i)
#se suma 1 al contador si el número fue par
		contador+=1
#se imprimen los numeros pares que se guardaron en contador
print(f"Total de números pares: {contador}")