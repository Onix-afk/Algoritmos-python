"""
Se requiere determinar cuál de tres cantidades proporcionadas es la mayor.
"""
"""Se piden 3 numeros"""
n1=float(input("Ingresa un número"))
n2=float(input("Ingresa un número"))
n3=float(input("Ingresa un número"))
"""Se busca si el primer numero es mayor"""
if (n1>n2):
   if(n1>n3):
   	  print(f"{n1} es mayor")
   else: 
   	  print(f"{n3} es mayor")
"""Se busca si el segundo numero es mayor"""
elif(n2>n1):
	if(n2>n3):
		print(f"{n2} es mayor")
	else:
		print(f"{n3} es mayor")
"""Se busca si el tercer numero es mayor"""
elif(n3>n2):
	if(n3>n1):
		print(f"{n3} es mayor")
	else:
		print(f"{n1} es mayor")
"""Se muestra un mensaje si los tres numeros son iguales"""
else:
	print(f"los numeros son iguales")