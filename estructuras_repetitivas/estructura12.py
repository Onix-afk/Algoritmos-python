"""
Cálculo de comisión decreciente para vendedores: Un vendedor realiza  ventas. 
Por cada venta mayor a $1,500 obtiene una comisión del 10%; para ventas entre 
$500 y $1,500 la comisión es del 5%, y para ventas menores a $500 no recibe 
comisión. Determina el total percibido por comisiones y el monto de la mayor venta 
realizada. 
"""
#se pide la cantidad de ventas
N=int(input("Número de ventas realizadas: "))
#se crean acumuladores para el total de comisiones y la venta mayor
total_com=0
mayor_venta=0
#se crea un ciclo que de vueltas por cada venta
for i in range(N):
#se pide el monto de la venta en cada vuelta
	venta=float(input(f"Monto de venta{i+1}: $"))
#si venta es mayor a la venta mayor, mayor venta agarra el valor de venta  
	if venta>mayor_venta:
		mayor_venta=venta
#si venta es mayor a 1500, la comision sera el 10% 
	if venta>1500:
		comision=venta*0.10
#si la venta es entre 500 y 1500, la comision es de 5% 
	elif venta>=500:
		comision=venta*0.05
#si la venta es menor a 500, no hay comision
	else:
		comision=0
#el total de comisiones se calcula sumando las comisiones de cada venta
	total_com+=comision
#se muestra el total de comisiones y la venta mas grande
print(f"Total en comisiones: ${total_com}")
print(f"La mayor venta fue: ${mayor_venta}")