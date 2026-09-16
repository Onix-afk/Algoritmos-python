"""
Fábricas "El cometa" produce articulos con claves(1,2,3,4,5 y 6).Se requiere un
 algoritmo para calcular los precios de venta, para esto hay que considerar lo
siguiente:
*Costo de producción=materia prima+mano de obra+gastos de fabricación.
*Precio de venta=costo de producción+45% de costo de producción
*El costo de la mano de obra se obtiene de la siguiente forma:para los productos
 con clave 3 o 4 se carga 75% del costo de la materia prima;para los que tienen
 clave 1 y 5 se carga 80%,y para los que tienen clave 2 o 6,85%.
Para calcular el gasto de fabricación se considera que si el articulo que se va 
 a producir tiene claves 2 o 5, este gasto representa 30% sobre el costo de la 
materia prima;si las claves son 3 o 6,representa 35%;si las claves son 1 o 4,re-
presenta 28%.La materia prima tiene el mismo costo para cualquier clave.
"""
#solicitar que se ingrese la clave del producto
clave=int(input("Ingresa la clave del producto(1-6): "))
#solicitar el costo de la materia prima
materia_prima=float(input("Ingresa el costo de la materia prima: $"))
#Se determina el costo de la mano de obra segun la clave
if clave in (3,4):
#si la clave es 3 o 4, la mano de obra es el 75% del costo de la materia prima
	mano_obra=materia_prima*0.75
elif clave in (1,5):
#si la clave es 1 o 5, es el 80%
	mano_obra=materia_prima*0.80
elif clave in (2,6):
#si la clave es 2 o 6, es el 85%
	mano_obra=materia_prima*0.85
else:
#si la clave no existe se muestra un mensaje de error
	print("Clave inválida")
	exit()
#se calcula los gastos de fabricación según la clave
if clave in (2,5):
#si la clave es 2 o 5, se suma la materia prima + 30% de materia prima
	gastos_fabricacion=materia_prima+(materia_prima*0.30)
elif clave in (3,6):
#si la clave es 3 o 6, materia prima + 35% de materia prima
	gastos_fabricacion=materia_prima+(materia_prima*0.35)
elif clave in (1,4):
#si la clave es 1 o 4, materia prima + 28% de materia prima
	gastos_fabricacion=materia_prima+(materia_prima*0.28)
#se suman los 3 gastos para obtener el costo total de la producción
costo_produccion=materia_prima+mano_obra+gastos_fabricacion
#para el precio de venta se multiplica el costo de producción por 1.45(45% de ganancia)
precio_venta=costo_produccion*1.45
#se muestran los resultados
print(f"Clave del producto: {clave}")
print(f"Materia prima: {materia_prima}")
print(f"Mano de obra: {mano_obra}")
print(f"Gastos de fabricación: {gastos_fabricacion}")
print(f"Costo de´producción: {costo_produccion}")
print(f"Precio de venta: {precio_venta}")