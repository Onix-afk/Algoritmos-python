"""
Rendimiento de un vehículo por trayecto: En un viaje de 8 etapas, se registra la 
distancia recorrida (en km) y el combustible consumido (en litros) de cada etapa. 
Calcula el consumo promedio (km/l) de cada etapa, el total de km recorridos y el 
rendimiento promedio total del viaje. 
"""
#se crean acumuladores para la distancia y el combustible
suma_dis=0
suma_com=0
#se crea un ciclo de 8 vueltas
for i in range(8):
#se pide la distancia y el combustible en cada etapa
	distancia=float(input(f"Etapa{i+1} - Distancia(km): "))
	combustible=float(input(f"Etapa{i+1} - combustible(L): "))
#se suman las distancias y el combustible cada vuelta y se imprime
	suma_dis+=distancia
	suma_com+=combustible
	print()
#se calcula el consumo promedio 
	consumo_prom=suma_dis/suma_com
#se muestra la distancia recorrida, el combustible consumido y el consumo promedio
print(f"Distancia recorrida total(km): {suma_dis}Km")
print(f"Consumo promedio por Litro: {consumo_prom}Km/L")
print(f"Rendimiento total del viaje: {consumo_prom}Km/L")