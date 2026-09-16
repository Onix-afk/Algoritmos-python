"""
La política de la compañía telefónica "chimefón" es: "Chismea +x-".
Cuando se realiza una llamada, el cobro es por el tiempo que ésta 
dura, de tal forma que los primeros cinco minutos cuestan $1.00 peso
c/u, los siguientes tres, 80c centavos de peso c/u, los siguientes
dos minutos, 70c centavos de peso c/u, y a partir del décimo minuto, 
50c centavos de peso c/u.
Además, se carga un impuesto de 3% cuando es domingo, y si es día hábil,
en turno matutino, 15%, y en turno vespertino, 10%.Realice un algoritmo
para determinar cuánto debe pagar por cada concepto una persona que 
realiza una llamada en moneda nacional mexicana(MXN).
"""
minutos=int(input("Minutos de la llamada: "))
if minutos<=5:
	costo_base=minutos*1.00
elif minutos<=8:
	costo_base=5*1.00+(minutos-5)*0.80
elif minutos<=10:
	costo_base=5*1.00+3*0.80+(minutos-8)*0.70
else:
	costo_base=5*1.00+3*0.80+2*0.70+8+(minutos-10)*0.50
"""Se selecciona el dia y se calcula el impuesto del dia"""
print("Seleccione el día:")
print("1-Domingo  2-Día hábil")
opcion_dia=int(input("Opción: "))
if opcion_dia==1:
	impuesto=0.03
	print("Es domingo, el impuesto es de 3%")
else:
"""si es dia habil se selecciona el turno"""
	print("Seleccione el turno:")
	print("1-Matutino  2-Vespertino")
	opcion_turno=int(input("Opción: "))
	if opcion_turno==1:
		impuesto=0.15
		print("Día hábil, turno matutino, el impuesto es de 15%")
	else:
		impuesto=0.10
		print("Día hábil, turno vespertino, el impuesto es de 10%")
"""se calcula el monto y el total a pagar"""
monto_impuesto=costo_base*impuesto
total=costo_base+monto_impuesto
"""se muestran los resultados"""
print(f"Subtotal: ${costo_base}")
print(f"Impuesto: ${monto_impuesto}")
print(f"Total a pagar: ${total}")














