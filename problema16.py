"""
Una aseguradora clasifica los vehiculos por tipo (A:Sedán,B:Camioneta,C:Motocicleta)
 y modelo por año.
*El valor base de la póliza se determina según el valor comercial del vehículo:
para tipo A es el 3.5% del valor comercial;para tipo B es el 4.8%;para tipo C
es el 6.2%.
*Recargo por antiguedad:Si el modelo es anterior al año 2015,se suma un recargo
 del 18% sobre el valor base de la póliza.Si es entre 2015 y 2020,el recargo es
 del 8%.Modelos posteriores a 2020 no tienen recargo.
*Descuento por historial:Si la edad del conductor es menor de 25 años,se aplica
 un recargo de riesgo del 12% sobre la póliza acumulada;si tiene 25 años o más,
 se descuenta un 5%.
*Salida:Calcular e imprimir el costo base de la póliza,recargos/descuentos apli-
cados y el costo total anual 
"""
#se solicita el tipo de vehiculo
tipo=input("Tipo de vehículo (A=Sedán, B=Camioneta, C=Motocicleta): ").upper()
#se solicita el valor comercial del vehiculo
Valor_comercial=float(input("Valor comercial del vehículo: $"))
#se solicita el año del modelo y la edad del conductor
modelo=int(input("Año del modelo: "))
edad_conductor=int(input("Edad del conductor: "))
#se calcula el valor base de la poliza segunel tipo de vehiculo
if tipo =='A':
#el Sedán es 3.5% del valor comercial
	valor_base=Valor_comercial*0.035
elif tipo =='B':
#la Camioneta es 4.8% del valor comercial
	valor_base=Valor_comercial*0.048
elif tipo =='C':
#la motocicleta es 6.2% del valor comercial
	valor_base=Valor_comercial*0.062
else:
#si escribe algo diferente se muestra un mensaje de error
	print("Tipo inválido")
	exit()
#se calcula el recargo por antiguedad del vehiculo
if modelo < 2015:
#si el modelo es anterior a 2015, +18% sobre el valor base
	recargo_antiguedad=valor_base*0.18
elif 2015 <= modelo <= 2020:
#si el modelo es entre 2015 y 2020, +8% sobre el valor base
	recargo_antiguedad=valor_base*0.08
else:
#si el modelo es 2021 o posterior, no hay recargo
	recargo_antiguedad=0.0
#el costo intermedio se obtiene sumando valor base y recargo
poliza_intermedia=valor_base+recargo_antiguedad
#Ajuste según edad del conductor
if edad_conductor<25:
#si es menor de 25 años +12% por riesgo
	ajuste_edad=poliza_intermedia*0.12
	tipo_ajuste="Recargo por riesgo"
else:
#si mayor de 24 años -5% por buen historial
	ajuste_edad=poliza_intermedia*(-0.05)
	tipo_ajuste="Descuento por historial"
#se suma todo para obtener el costo final anual
total_anual=poliza_intermedia+ajuste_edad
#se muestran los resultados
print(f"Valor base de la póliza: ${valor_base}")
print(f"Recargo por antiguedad: ${recargo_antiguedad}")
print(f"{tipo_ajuste}: ${ajuste_edad}")
print(f"Costo total anual: ${total_anual}")