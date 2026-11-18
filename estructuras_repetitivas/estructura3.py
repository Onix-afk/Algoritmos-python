"""
Inversión con interés compuesto anual: Un inversionista inicia con un capital inicial 
de $2,000 y recibe un rendimiento del 8% anual acumulado durante  años. Genera 
un reporte que muestre el capital ganado en cada uno de los años y el saldo final 
acumulado al terminar el periodo.
"""
#esta sera la capital inicial que inicia en 2000
capital=2000.0
#este sera el rendimiento anual
tasa=0.08
#se pide la cantidad de años que se hara la inversion
años=int(input("¿Número de años de la inversión?: "))
print(f"Año|Capital inicial|Ganancia|Saldo al final")
#el saldo va a ser la capital
saldo=capital
#se crea un ciclo que de vueltas por la cantidad de años ingresados 
for año in range(1,años+1):
#la gancia va a ser el 8% del saldo
	ganancia=saldo*tasa
#se suma la ganancia en el saldo
	saldo+=ganancia
	print(f"{año:4}|${capital:.2f}|${ganancia:.2f}|${saldo:.2f}")
#capital agarra el valor del saldo anterior
	capital=saldo
#se muestra el saldo despues de la cantidad de años ingresados
print(f"saldo final después de {años} años: ${saldo:.2f}")