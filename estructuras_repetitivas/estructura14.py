"""
Actualización de precios por inflación: Una lista de  productos tiene sus precios 
actuales. La empresa aplicará un aumento del 5% a los productos que cuesten 
menos de $100, un 8% a los que cuesten entre $100 y $500, y un 12% a los 
mayores de $500. Imprime el costo anterior, el nuevo costo de cada producto y la 
diferencia total sumada del ajuste.
"""
#se pide la cantidad de productos 
N=int(input("Ingrese la cantidad de productos: "))
#se crea un acumulador
total_diferencia=0
print("Producto | Precio Antiguo | Precio Nuevo | Diferencia")
#se crea un ciclo que de vueltas por cada producto
for i in range(1, N+1):
#se pide el precio del producto en cada vuelta
	precio=float(input(f"Precio del producto {i}: $"))
#si el precio cuesta $100 o menos se aplica un descuento del 5%
	if precio<100:
		aumento=0.05
#si el precio es entre $100 y $500 se aplica un descuento del 8%
	elif precio<=500:
		aumento=0.08
#si el precio es mayor a $500 se aplica un descuento del 12%
	else:
		aumento=0.12
#el precio nuevo sera el precio con el aumento
	nuevo=precio*(1+aumento)
#se calcula la diferencia entre el precio nuevo y el viejo
	diferencia=nuevo-precio
#la diferencia total es la suma de las diferencias de cada producto
	total_diferencia+=diferencia
#se van mostrando el numero del producto, el precio anterior y nuevo, y la diferencia
	print(f"{i:^7} | ${precio:14.2f} | ${nuevo:12.2f} | ${diferencia:10.2f}")
#se muestra la diferencia total
print(f"Diferencia total del ajuste: ${total_diferencia:.2f}")