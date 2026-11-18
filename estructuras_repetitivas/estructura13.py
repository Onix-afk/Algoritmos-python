"""
Control de producción por turnos: Una fábrica registra la cantidad de piezas 
producidas por 3 turnos (Mañana, Tarde y Noche) a lo largo de 7 días. Acumula la 
producción total de cada turno al final de la semana e indica cuál fue el turno más 
productivo.
"""
#se declaran los dias de la semana en un
dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
#se crean acumuladores para mañana,tarde y noche
mañana=0
tarde=0
noche=0
#se crea un ciclo para los dias
for dia in dias:
#se pide la cantidad de piezas por cada turno cada dia y se van imprimiendo en cada vuelta
	m=int(input(f"{dia} - Turno Mañana: "))
	t=int(input(f"{dia} - Turno Tarde: "))
	n=int(input(f"{dia} - Turno Noche: "))
	print()
#cada uno se registra en su acumulador
	mañana+=m
	tarde+=t
	noche+=n
#se muestra el total de cada turno
print(f"Total turno Mañana: {mañana}")
print(f"Total turno Tarde: {tarde}")
print(f"Total turno Noche: {noche}")
#se busca el mayor entre los tres turnos
mayor=max(mañana,tarde,noche)
#si mañana es el mayor se muestra un mensaje que dice que es el mas productivo
if mayor==mañana:
	print("El turno mas productivo fue el turno de la Mañana")
#si tarde es el mayor se muestra un mensaje que dice que es el mas productivo
elif mayor==tarde:
	print("El turno mas productivo fue el turno de la Tarde")
#si noche es el mayor se muestra un mensaje que dice que es el mas productivo
else:
	print("El turno mas productivo fue el turno de la Noche")