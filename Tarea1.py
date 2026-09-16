"""
El director de una escuela está organizando un viaje de estudios, y 
requiere determinar cuánto debe cobrar a cada alumno y cuánto debe 
pagar a la compañía de viajes por el servicio. La forma de cobrar
es la siguiente: si son 100 alumnos o más, el costo por cada alumno
es de $65.00; de 50 a 99 alumnos, el costo es de $70.00, de 30 a 49,
de $95.00, y si son menos de 30, el costo de la renta del autobús es
de $4000.00, sin importar el número de alumnos.
"""
try:
#se pide la cantidad de alumnos 
	Alumnos = int(input("¿cuál es la cantidad de alumnos?"))
#Si hay 100 alumnos o mas cada uno paga $65
	if (Alumnos >= 100):
		total =Alumnos *65
#si hay entre 50 y 99 alumnos cada uno paga $70
	elif (Alumnos >= 50):
		total =Alumnos *70
#si hay entre 30 y 49 alumnos cada uno paga $95
	elif (Alumnos >= 30):
		total =Alumnos *95
#si hay menos de 30 alumnos se paga $4000 por el autobus
	else:
		total = 4000
#se muestra el monto a pagar
	print(total)
#se muestra un mensaje de error si el usuario no escribe un numero positivo
except:
	print("solo puedes ingresar numeros positivos")