"""
La compañia de autobuses "La curva loca" requiere determinar el costo que tendrá el boleto de un viaje 
sencillo, esto basado en los kilómetros por recorrer y en el costo por kilómetro.
Costo por km:$80.00mxn
"""
"""se piden los kilometros a viajar"""
kilometros=int(input("¿Cuantos kilometros va a viajar?"))
"""se define el precio por cada kilometro"""
costo_kilometros=80
"""se calcula el total a pagar por los kilometros viajados"""
cobro=kilometros*costo_kilometros
"""se muestra el resultado"""
print(f"Va a pagar: {cobro}")