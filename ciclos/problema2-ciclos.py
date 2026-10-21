#Mostrar la tabla de multiplicar de un n numero ingresado por teclado
"""se hace un input para que el usuario ingrese el
numero del que desea saber la tabla """
n=int(input("Ingresa un número: "))
#se crea un for que muestre 10 resultados e inicie en 1
for i in range(1,11):
"""se imprime (el numero ingresado)x(la vuelta correspondiente)=
 (el numero ingresado)*(el numero de vuelta correspondiente)"""
	print(f"{n}x{i}={n*i}")