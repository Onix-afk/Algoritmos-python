"""
Categorización de ventas con montos acumulados: Procesa  ventas realizadas en 
un negocio. El programa debe determinar cuántas ventas fueron menores o iguales 
a $300, cuántas entre $301 y $800, y cuántas mayores a $800. Debe mostrar la 
cantidad de ventas y el monto total recaudado en cada categoría, además del total 
general.
"""
#se piden las ventas que se van a registrar
N=int(input("¿Cuántas ventas vas a registrar?: "))
#se crean acumuladores para las ventas menores o iguales a 300, las ventas entre 301 y 800 y para las ventas mayores a 800
menor_igual=0
entre=0
mayor=0
#se crean acumuladores para el total de cada categoria de venta
total_menor=0
total_entre=0
total_mayor=0
#se crea un ciclo que de vueltas segun la cantidad de ventas registradas
for i in range(1,N+1):
#se pide el monto de cada vuelta
	monto=float(input(f"Monto de la venta: $"))
#si el monto es menor o igual a 300 se suma al acumulador menor_igual y el monto se suma al acumulador total_menor
	if monto<=300:
		menor_igual+=1
		total_menor+=monto
#si el monto es entre 301 y 800 se suma al acumulador entre y el monto se suma al acumulador total_entre
	elif monto<=800:
		entre+=1
		total_entre+=monto
#si el monto es mas de 800 se suma al acumulador mayor y el monto se suma al acumulador total_mayor
	else:
		mayor+=1
		total_mayor+=monto
#se  muestra la cantidad de ventas de $300 o menos y la ganancia de esas ventas
print(f"===============================================")
print(f"Ventas de $300 o menos: {menor_igual}")
print(f"dinero de las ventas de $300 o menos: {total_menor}")
#se  muestra la cantidad de ventas de $301 a $800 y la ganancia de esas ventas
print(f"===============================================")
print(f"ventas de $301 a $800: {entre}")
print(f"dinero de las ventas de $301 a $800: {total_entre}")
#se  muestra la cantidad de ventas de mayores a $800 y la ganancia de esas ventas
print(f"================================================")
print(f"ventas de mas de $800: {mayor}")
print(f"dinero de las ventas de mas de $800: {total_mayor}")
#se mustra el total ganado por todas las ventas
print(f"================================================")
print(f"Total de ventas: ${total_menor + total_entre + total_mayor:.2f}")