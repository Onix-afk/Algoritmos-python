"""
Realizar un algoritmo para determinar cuánto ahorrará una persona
en un año, si al final de cada mes deposita cantidades variables
de dinero; además, se quiere saber cuánto lleva ahorrado cada mes. 
"""
#se crea un contador para lo que ahorro en total
ahorro_total=0
#se crea un ciclo de 12 vueltas
for mes in range(12):
#se pide el monto depositado en cada mes
	deposito=float(input(f"mes{mes+1} - Ingresa el monto a depositar: "))
#el monto depositado se suma al contador
	ahorro_total+=deposito
#se muestra lo que lleva ahorrado en cada mes
	print(f"Al mes {mes+1} llevas ahorrado: ${ahorro_total:.2f}")
#se muestra lo que ahorro en un año
print(f"\nTotal ahorrado en un año: ${ahorro_total:.2f}")