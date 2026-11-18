"""
Plan de ahorro mensual con meta variable: Una persona desea ahorrar dinero mes a 
mes durante un año. Al final de cada mes ingresa el monto depositado. El programa 
debe mostrar el acumulado mes tras mes y, al finalizar los 12 meses, indicar si logró 
superar una meta fija de $12,000 y por cuánto la superó o cuánto le faltó. 
"""
#la meta a llegar sera 12000
meta=12000
#se crea un acumulador que guarde el deposito de cada mes
acumulado=0
#se crea un ciclo de 12 vueltas
for mes in range(1,13):
#se pide el deposito cada mes y se suma en el acumulador
	desposito=float(input(f"Deposito del mes{mes}: $"))
	acumulado+=desposito
#se muestra el dinero acumulado hasta ese momento
	print(f"acumulado hasta ahora: ${acumulado:.2f}")
#al final se muestra el dinero acumulado en 12 meses
print(f"total ahorrado: ${acumulado:.2f}")
#se muestra un mesaje si se alcanzo la meta y por cuanto dinero se supero
if acumulado>=meta:
	print(f"¡Meta alcanzada! Superaste la meta por ${acumulado-meta:.2f}")
#se muestra un mensaje sino se alcanzo la meta y cuanto dinero falto
else:
	print(f"No se alcanzo la meta. Faltaron ${meta-acumulado:.2f}")