"""
Un empleado de la tienda "Tiki Taka" realiza N ventas durante el día, se requiere saber
cuántas de ellas fueron mayores a $1000, cuántas fueron mayores a $500 pero menores o 
iguales a $1000, y cuántas fueron menores o iguales a $500. Además, se requiere saber 
el monto de lo vendido en cada categoría y de forma global. Realice un algoritmo que 
permita determinar lo anterior.
"""
#se crean contadores para los precios mayor a 1000,entre 500 y 100, menor de 500
mayor_1000=0
mayor_500=0
menor_500=0
#se crean contadores para la suma de cada categoria
total_mayor_1000=0
total_mayor_500=0
total_menor_500=0
#se pide la cantidad de valores que va a ingresar
N=int(input("¿Cuántas ventas se realizaron hoy?: "))
#se crea un ciclo que de la cantidad de vueltas indicada en el input
for i in range(N):
#se pide el valor de cada venta
	venta=float(input(f"Ingresa el monto de la venta {i+1}: $"))
#se verifica si la venta es mayor a 1000, esta entre 500 y 1000 o si es menor a 500
#se 1 segun la categoria de la venta y se suma el valor de la venta a su respectiva categoria 
	if venta>1000:
		mayor_1000+=1
		total_mayor_1000+=venta
	elif venta>500:
		mayor_500+=1
		total_mayor_500+=venta
	else:
		menor_500+=1
		total_menor_500+=venta
#se calcula el total de la suma de todas las ventas
total_general=total_mayor_1000+total_mayor_500+total_menor_500
#se muestra cantidad de ventas mayores a 1000 y su valor en $
print(f"Ventas mayores a $1000: {mayor_1000} | Total: ${total_mayor_1000}")
#se muestra cantidad de ventas entre 500 y 1000 y su valor en $
print(f"Ventas mayores a $500 y menores a $1000: {mayor_500} | Total: ${total_mayor_500}")
#se muestra cantidad de ventas menores a 500 y su valor en $
print(f"Ventas menores o iguales a $500: {menor_500} | Total: ${total_menor_500}")
#se muestra el total de la suma de todas las ventas
print(f"Total de ventas: {total_general}")