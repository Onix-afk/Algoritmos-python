"""
Determina cuánto se debe pagar por equis cantidad de lápices considerando
que si son 1000 o más el costo es de $0.85; de lo contrario, el precio es
de $0.90
"""
"""Se pide la cantidad de lapices a comprar"""
Cant=int(input("Cuantos lapices vas a comprar"))
"""Se calcula el precio según la cantidad de lapices"""
if (Cant >= 1000):
      pago=Cant*0.85
else:
	   pago=Cant*0.90
"""Se muestra el total a pagar"""
print(f"va a pagar: {pago}")