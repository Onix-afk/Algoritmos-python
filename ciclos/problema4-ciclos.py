"""
Pide al usuario queingrese N números enteros uno por uno.
Al finalizar la lectura, muestra la suma total de todos
los números ingresados
"""
#se crea un input que pida la cantidad de números a ingresar
n=int(input("¿Cuántos números deseas ingresar?: "))
#se crea la variable suma que inicia en 0
suma=0
#se crea un for que de la cantidad de vueltas ingresadas en el input
for i in range(n):
#se crea un input donde ingrese un numero por cada vuelta
	num=int(input(f"Ingresa el número{i+1}: "))
#los numeros se suman en la variable suma
	suma+=num
#se imprime el resultado de la suma
print(f"La suma totla es: {suma}")
