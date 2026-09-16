"""
repaso-Problema 3
Un estacionamiento require determinar el cobro que debe aplicar a las personas que lo utilizan. Considere que
el cobro es con base en las horas que lo disponen y que las fracciones de hora se toman como completas.
"""
"""se importa la libreria math"""
import math
"""se pide el tiempo que se estuvo en el estacionamiento"""
minutos_estancia=int(input("¿Cuanto tiempo estuvo en el estacionamiento? "))
"""se define el precio por hora"""
precio_hora=20
"""se convierten los minutos a horas"""
redondeo=math.ceil(minutos_estancia/60)
"""Se calcula el total a pagar"""
cobro=precio_hora*redondeo
"""Se muestra el resultado"""
print(f"Debe pagar: {cobro}")