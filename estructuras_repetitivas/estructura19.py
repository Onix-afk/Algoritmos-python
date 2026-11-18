"""
Sensor de nivel de depósito con alerta: Un tanque de agua de 1,000 litros recibe 
descargas periódicas de agua. En cada ciclo se ingresa el volumen en litros de cada 
descarga hasta que el tanque alcance o supere el 95% de su capacidad total. 
Reporta cuántas descargas se necesitaron y el volumen total almacenado. 
"""
#se establece la capacidad del tanque
capacidad=1000
#se establece el limite al que se detendra(95%)
limite=capacidad*0.95
#se crean contadores
descargas=0
total_almacenado=0
nivel_actual=0
#mientras el nivel sea menor al 95%, se pide el volumen de la descarga actual
while nivel_actual<limite:
	volumen=float(input(f"Ingrese el volumen de descarga {descargas+1} (litros): "))
#verificamos que al agregar no se pase del limite
	if nivel_actual+volumen<=limite:
#se suma el volumen al nivel del tanque
		nivel_actual+=volumen
#se acumula el total de litros y se cuenta la descarga
		total_almacenado+=volumen
		descargas+=1
#Si se pasa del limite, avisa y no se permite la descarga
	else:
		print("El volumen excede el limite permitido. Intentecon una cantidad menor")
#se muestran las descargas que se ocuparon, el volumen total almacenado y el nivel final
print(f"Descargas necesarias: {descargas}")
print(f"Volumen total almacenado: {total_almacenado} litros")
print(f"Nivel final del tanque: {nivel_actual} litros(95%)")