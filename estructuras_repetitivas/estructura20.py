"""
Procesamiento de facturas vencidas: Un departamento de cobranza procesa  𝑁
facturas. Por cada una se lee el monto original y los días de retraso. Si los días de 
retraso son mayores a 30, se le aplica un recargo del 5%; si son mayores a 60 días, 
el recargo es del 12%. Muestra el importe corregido de cada factura y el monto 
acumulado por penalizaciones.
"""
#se pide el numero de facturas a procesar
n=int(input("Ingrese el número de facturas a procesar: "))
#se crea un acumulador para las penalizaciones
monto_acumulado_penalizaciones=0
#se crea un ciclo que de vueltas segun el numero de facturas
for i in range(n):
#se pide el monto original y los dias de retraso por cada factura	
	monto_original=float(input(f"Factura{i+1} - Monto original: $"))
	dias_retraso=int(input(f"Factura {i+1} - Días de retraso: "))
#si los dias de retraso son mas de 60 el recargo es el monto ingresado por 0.12
	if dias_retraso>60:
		recargo=monto_original*0.12
#si los dias de retraso son menos de 30 el recargo es el monto ingresado por 0.05
	elif dias_retraso<30:
		recargo=monto_original*0.05
#si no el recargo es 0
	else:
		recargo=0
#se calcula el importe corregido sumando el monto ingresado mas el recargo
	importe_corregido=monto_original+recargo
#se calcula el monto acumulado sumando los recargos
	monto_acumulado_penalizaciones+=recargo
#se muestra el importe de la factura corregido 
	print(f"Importe corregido de la factura: ${importe_corregido:.2f}")
#se muestra el total de las penalizaciones
print(f"Monto acumulado total por penalizaciones: ${monto_acumulado_penalizaciones:.2f}")