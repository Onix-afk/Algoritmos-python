"""
Una compañía fabrica focos de colores(verdes,blancos y rojos). Se desea
contabilizar, de un lote de N focos, el número de focos de cada color 
que hay en existencia 
"""
#se pide el total de focos a verifcar
N=int(input("Ingresa el total de focos en el lote: "))
#se crea un contador por cada color de foco
verdes=0
blancos=0
rojos=0
#se crea un ciclo donde la cantidad de vueltas es el total de focos
for i in range(N):
#se pide el color de cada foco
	color=input(f"Ingresa el color del foco {i+1} (verde,blanco,rojo): ")
#se verifica el color del foco y se suma a su respectivo contador
	if color=="verde":
		verdes+=1
	elif color=="blanco":
		blancos+=1
	elif color=="rojo":
		rojos+=1
#si no se ingresa uno de los 3 colores se muestra un mensaje de error
	else:
		print("color no valido")
#se muestra el total de focos de cada color
print(f"Verdes: {verdes}")
print(f"Blancos: {blancos}")
print(f"Rojos: {rojos}")