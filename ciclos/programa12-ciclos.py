"""
Realizar un algoritmo que pida N números(se pedirá por teclado
la cantidad de números a introducir). El programa debe informar 
de cuantos números introducidos son mayores que 0, menores que 0
e iguales a 0.
"""
#se crea un contador para los numeros mayores a 0
may=0
#se crea un contador para los numeros menores e iguales a 0
men=0
num1=0
#se pide la cantidad de números a ingresar
n = int(input("Dime cauntos numeros vas a ingresar: "))
#se crea un ciclo que de la cantidad de vueltas escritas en el input
for i in range(n):
#se pide el numero 
	num1 = int(input(f"ingresa el num{i+1}: "))
#se verifica si el numero es mayor o menor a 0 y se guarda en su contador especifico
	if(num1 > 0):
		may +=1
	else:
		men +=1
#se muestra el total de numeros mayores a 0
print(f"numeros mayores:{may}")
#se muestra el total de numeros menores e iguales a 0
print(f"numeros menores o iguales a 0:{men}")