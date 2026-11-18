"""
Simulación de nómina semanal con horas extras: Pide las horas trabajadas cada día 
durante 6 días por un empleado. Si en un día supera las 8 horas, las horas 
adicionales se pagan al doble de la tarifa normal por hora. Calcula el sueldo total 
semanal y el número total de horas extras trabajadas.
"""
#se pide la tarifa que cobra por hora
tarifa_normal=float(input("Ingresa la tarifa por hora normal: $"))
#se crean acumuladores para las horas extras y para el sueldo
horas_extras_tot=0
tot_sueldo=0
#se crea un ciclo que de 6 vueltas
for dia in range(1,7):
#se pide las horas trabajadas cada dia
	horas=float(input(f"\nHoras trabajadas en el dia{dia}: "))
"""si las horas ingresadas son mayores a 8, se restan 8 horas de las horas ingresadas y el resultado 
se guarda en horas_extras, horas_extras se suma al acumulador de horas extras"""
	if horas>8:
               hora_normal=8
               horas_extras=horas-8
               horas_extras_tot+=horas_extras
"""si las horas ingresadas son menos de 9 se guardan en hora_normal y no se guarda un cero en horas_extras"""
	else:
                hora_normal=horas
                horas_extras=0
"""se calcula el sueldo del dia multiplicando las horas menores a 9 por la tarifa ingresada y eso se suma a 
el doble de la tarifa ingresada que se multiplica por las horas extras"""
	sueldo_dia=hora_normal*tarifa_normal+horas_extras*tarifa_normal*2
#se calcula el sueldo de la semana sumando el sueldo de cada dia
	tot_sueldo+=sueldo_dia
#se muestra el dia y el sueldo de ese dia
	print(f"Sueldo del dia{dia}: {sueldo_dia}")
#se muestra el seuldo de la semana y el total de horas extras 
print(f"sueldo total: ${tot_sueldo}")
print(f"total de horas extras: {horas_extras_tot} horas")
