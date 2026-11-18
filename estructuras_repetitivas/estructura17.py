"""
Tabla de amortización simplificada: Para un préstamo de valor  diferido a  meses, 
calcula el pago de capital constante más un interés mensual fijo del 1.5% sobre el 
saldo insoluto. Muestra la tabla mes a mes con la cuota a pagar y el saldo restante. 
"""
#se pide el valor del prestamo y el numero de meses en los que se va a pagar
valor_pretamo=float(input("Valor del prestamo: $"))
meses=int(input("Número de meses: "))
#la tasa mensual del 15%
tasa_mensual=0.015
#se divide el valor de prestamo entre los meses para obtener el capital mensual
capital_mensual=valor_pretamo/meses
#el saldo va a ser el valor de prestamo
saldo=valor_pretamo
#se hace un print para la tabla
print("Mes | Cuota mensual | Interés | Capital | Saldo restante")
#se crea un ciclo que de vueltas por cada mes
for mes in range(1,meses+1):
#el interes se obtiene sacando el 15% del saldo
	interes=saldo*tasa_mensual
#la cuota es la capital mensual + interes
	cuota_total=capital_mensual+interes
#la capital mensual se resta al capital
	saldo-=capital_mensual
#se van mostrando los resultados
	print(f"{mes:3} | ${cuota_total:12.2f} | ${interes:7.2f} | ${capital_mensual:7.2f} | ${saldo:14.2f}")