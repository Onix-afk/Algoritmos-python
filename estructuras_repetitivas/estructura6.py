"""
Control de peso y sobrepeso en envíos: Se recibe un lote de  paquetes. Se debe 
registrar el peso de cada uno en kg. Si un paquete pesa más de 15 kg, se le aplica 
un recargo de $50 de transporte. Muestra cuántos paquetes tenían sobrepeso, el 
total pagado en recargos y el peso medio de todo el lote.
"""
#se pide el numero de paquetes
N=int(input("Ingresa el número de paquetes: "))
#el peso limite es 15kg
limite=15
#recargo de 50 si es mas pesado
recargo=50
#acumuladores para la cantidad de paquetes con peso extra,total de recargos y la suma de los pesos 
sobrepeso=0
tot_rec=0
suma_pesos=0
#se crea un ciclo que de vuelta por cada paquete registrado
for i in range(N):
#se pide el peso por cada paquete
	peso=float(input(f"Ingrese el peso del paquete {i+1}: "))
#el peso se suma en el acumulador de los pesos
	suma_pesos+=peso
#si el peso es mayor a 15 se suma 1 a sobrepeso y 50 a el total de recargos
	if peso >limite:
		sobrepeso+=1
		tot_rec+=recargo
#se calcula el peso promedio dividiendo la suma de todos los pesos entre la cantidad de paquetes
peso_prom=suma_pesos/N
#se muestra la cantidad de paquete con sobrepeso, el costo total de recargos y el peso promedio
print(f"Paquetes con sobrepeso: {sobrepeso}")
print(f"Total en recargos: ${tot_rec}")
print(f"Peso promedio del lote: {peso_prom}")