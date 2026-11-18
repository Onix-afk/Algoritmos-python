"""
Consumo de energía eléctrica y tarifas por escalón: Se registra el consumo de luz en 
kWh durante 6 bimestres. Si el consumo en un bimestre es menor o igual a 250 
kWh, la tarifa es de $1.5 por kWh; si supera los 250 kWh, el exceso se cobra a $2.8 
por kWh. Muestra el importe a pagar en cada bimestre y el gasto anual total. 
"""
#se pide el consumo de luz de un bimestre
consumo=float(input("Ingrese el consumo en Kwh del bimestre: "))
#si el consumo es menor o igual a 250 se cobra $1.5 por cada kwh
if consumo<=250:
	total=consumo*1.5
#si no el consumo es $2.8 por kwh
else:
#el exceso es el consumo-250 ya que el exceso seria de 251 en adelante
    exceso=consumo-250
#el total se calcula multiplicando 250*1.5  y sumarlo a el exceso*2.8
    total=(250*1.5)+(exceso*2.8)
#el total se multiplica por 6 para obtener el gasto en un año
gasto_anual=total*6
#se muestra el importe de cada bimestre y el gasto anual
print(f"Importe a pagar en este bimestre: ${total:.2f}")
print(f"Gasto anual estimado: ${gasto_anual:.2f}")
