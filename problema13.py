"""
La política de la compañía telefónica "chimefón" es: "Chismea +x-".
Cuando se realiza una llamada, el cobro es por el tiempo que ésta 
dura, de tal forma que los primeros cinco minutos cuestan $1.00 peso
c/u, los siguientes tres, 80c centavos de peso c/u, los siguientes
dos minutos, 70c centavos de peso c/u, y a partir del décimo minuto, 
50c centavos de peso c/u.a (MXN).
Determinar cuánto debe pagar por cada concepto una persona que realiza
una llamada en moneda nacional mexicana(MXN).
"""
"""Se pide la duración de la llamada"""
minutos=int(input("Minutos de la llamada: "))
"""si la llamada dura 5 minutos o menos se cobra $1 por minuto"""
if minutos<=5:
	total=minutos*1.00
"""si dura de 6 a 8 minutos se cobra $1 los primeros 5 minutos y $0.8 el resto"""
elif minutos<=8:
	total=5*1.00+(minutos-5)*0.80
"""si dura 9 o 10 minutos se cobra $1 los primeros 5 minutos, los siguentes 3 minutos a $0.8 y
$0.7 el resto""" 
elif minutos<=10:
	total=5*1.00+3*0.80+(minutos-8)*0.70
"""si dura mas de 10 minutos a lo anterior se le suman $0.5 por minuto a partir del  minuto 11"""
else:
	total=5*1.00+3*0.80+2*0.70+8+(minutos-10)*0.50
"""Se muestra el total a pagar"""
print(f"Total a pagar: ${total}")