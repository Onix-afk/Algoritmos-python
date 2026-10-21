"""
Diseñe una aplicación que permita ingresar n números y 
muestre y sume los números pares.
"""
#se hace un input que pide la cantidad de números a ingresar 
n=int(input("¿Cuántos números deseas ingresar?: "))
#se crea una variable que va a guardar la suma de los numeros par e inicie en 0
suma_par=0
#se crea una lista para guardar los números pares
pares=[]
#se crea un for que da vueltas la cantidad de veces indicada en el input
for i in range(n):
#se hace un input que pida numero por cada vuelta 
	num=int(input(f"Ingresa el numero{i+1}: "))
#verificamos si el número es par 
	if num%2==0:
#agregamos el número a la lista de pares
		pares.append(num)
#sumamos el número al total
		suma_par+=num
#se muestran los números pares ingresados
print("Los números pares ingresados fueron: ")
for p in pares:
	print(p)
#se muestra el total de la suma de los números pares ingresados
print(f"La suma de los números pares es: {suma_par}")