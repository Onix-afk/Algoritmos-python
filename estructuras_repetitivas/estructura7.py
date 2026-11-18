"""
Registro de temperaturas extremas y promedios: Registra las temperaturas máximas 
de cada día del mes (30 días). Determina cuál fue la temperatura más alta 
registrada, la más baja y calcula el promedio mensual de temperatura. 
"""
#se crea una lista vacia
temps=[]
#se crea un ciclo de 30 vueltas
for i in range(30):
#se pide la temperatura cada dia 
	t=float(input(f"Temperatura máxima del dia {i}: "))
#crea la lista de las temperaturas
	temps.append(t)
#se guarda la mayor temperatura, la minima y la temperatura promedio
alta=max(temps)
baja=min(temps)
prom=sum(temps)/len(temps)
#se muestran la temperatura mas alta,la mas baja y la promedio
print(f"Temperatura más alta: {alta}")
print(f"Temperatura más baja: {baja}")
print(f"Promedio mensual: {prom}")