"""
Se requiere determinar el costo que tendrá realizar una llamada telefónica con base en el tiempo que dura la 
llamada y en el costo por minuto.
costo por minuto:$3.00mxn
"""
"""se define el costo por minuto"""
min=3
""" se pide los minutos de duración de la llamada"""
llamada=int(input("¿Cuantos minutos duro su llamada?"))
"""se calcula el total a pagar"""
cobro= min*llamada
"""se muestra el resultado"""
print(f"Su llamada duro {llamada} minutos, se le cobrara $ {cobro}")