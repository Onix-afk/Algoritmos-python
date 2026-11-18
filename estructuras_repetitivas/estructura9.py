"""
Simulador de pago de tarjeta de crédito: Una deuda inicial de $10,000 genera un 
interés mensual del 2% sobre el saldo restante. Si el usuario realiza un pago fijo de 
$1,000 cada mes, calcula mediante un ciclo en cuántos meses liquidará 
completamente la deuda y cuánto pagó en total por concepto de intereses. 
"""
#se define el valor inicial de la deuda
deuda=10000
#se establece el pajo fijo de cada mes
pago_fijo=1000
#la tasa de interes mensual sera del 2%
int_men=0.02
#se crea un contador para los meses
meses=0
#contador para el pago total de los intereses
total_int=0
#mientras la deuda sea mayor a 0
while deuda>0:
#se calcula el interes del mes mes actual
	interes=deuda*int_men
#se van sumando el monto del interes
	total_int+=interes
#se suma el interes a la deuda
	deuda+=interes
#si la deuda es menor al pago fijo, se paga lo que resta
	if deuda<pago_fijo:
		pago_fijo=deuda
#se resta el pago del mes a la deuda y se incrementa el contador de meses
	deuda-=pago_fijo
	meses+=1
#se muestra la cantidad de meses y cuanto pago en total en intereses
print(f"Meses para liquidar: {meses}")
print(f"Total pagado en intereses: ${total_int}")