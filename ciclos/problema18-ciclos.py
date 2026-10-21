"""
Una empresa tiene el registro de las horas que trabaja diariamente
un empleado durante la semana(seis dias) y requiere determinar el
total de éstas, así como el sueldo que recibirá por las horas trabajadas
"""
#se pide el sueldo que gana por hora
sueldo=float(input("¿Cuánto gana por hora?: "))
#se crea un contador para las horas de la semana
total_horas=0
#se crea un ciclo de 6 vueltas
for dia in range(6):
#se pide las horas trabajadas cad dia
	horas=int(input(f"¿Cuántas horas trabajo el dia{dia+1}: "))
#las horas ingresadas se suman al contador
	total_horas+=horas
#se calcula el sueldo de la semana
	total_sueldo=total_horas*sueldo
#se muestra el total de horas que trabajo esta semana
print(f"El total de horas trabajadas en la semana es: {total_horas}")
#se muestra el sueldo de esta semana
print(f"El pago de esta semana es: ${total_sueldo}")