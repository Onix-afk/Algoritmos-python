"""
Validación e intentos de cobro en cajero: Un usuario intenta retirar dinero de un 
cajero que solo permite hasta 3 intentos fallidos por saldo insuficiente o clave 
incorrecta. Si el usuario ingresa un monto mayor a su saldo disponible (N), 
descuenta un intento. El ciclo termina si el retiro es exitoso o si agota sus 3 intentos.
"""
#se pide el saldo disponible en la cuenta
saldo=float(input("Ingrese el saldo disponible en la cuenta: $"))
#se crea un acumulador para los intentos
intentos=0
#se crea un False 
exito=False
#mientras los intentos sean menos de 3 y exito no se cumpla
while intentos<3 and not exito:
#se pide el monto que quiere retirar
	monto=float(input("Ingrese el monto que va a retirar: $"))
"""si el monto es mayor al saldo se cuenta un intento, se saca el 2% del monto 
para sacar el descuento y el descuento se resta al saldo"""
	if monto > saldo:
		intentos+=1
		descuento=monto*0.02
		saldo-=descuento
#se muetra un mensaje de saldo insuficiente, se muestra el descuento aplicado y se muestra el saldo actual
		print(f"Fondos insuficientes. Descuento aplicado: ${descuento:.2f}")
		print(f"Saldo actual: ${saldo:.2f}")
#si intentos son menos de 3, se imprime cuantos intentos le quedan
		if intentos<3:
			print(f"Le quedan {3-intentos} intentos")
"""si el monto es menor que el saldo, se resta el monto al saldo, se imprime un mensaje
de retiro exitoso y muestra cuanto retito y el saldo restante"""
	else:
		saldo-=monto
		print(f"Retiro exitoso. Entregado: ${monto:.2f}")
		print(f"Saldo restante: ${saldo:.2f}")
		exito=True
#si se agotan los intentos antes de poner un monto menor al saldo 
#muestra un mensajede intentos agotados y muestra el saldo final
if not exito:
	print("Se agotaron los 3 intentos. Operación cancelada.")
	print(f"Saldo final: ${saldo:.2f}")		