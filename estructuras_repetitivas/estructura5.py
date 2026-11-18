"""
Inventario y conteo por tipo de producto: En una bodega hay un lote de  artículos 
clasificados por su tipo mediante un código (1: Electrónica, 2: Ropa, 3: Alimentos). 
Cuenta cuántos artículos hay de cada tipo y calcula el porcentaje que representa 
cada categoría sobre el total. 
"""
#se pide la cantidad de articulos que se van a registrar
N=int(input("¿Cuántos articulos va a registrar?: "))
#se crean acumuladores para las 3 catergorias
electronica=0
ropa=0
alimentos=0
#se crea un ciclo que de vuelta por cada articulo registrado
for i in range(1,N+1):
#se muestra el numero para representar cada categoria
	print("1=Electrónica")
	print("2=Ropa")
	print("3=Alimentos")
#se introduce el numero del articulo a registrar
	codigo=int(input("Ingresa el código: "))
#si el codigo es 1 se suma 1 a el acumulador de electronica
	if codigo==1:
		electronica+=1
#si el codigo es 2 se suma 1 a el acumulador de ropa
	elif codigo==2:
		ropa+=1
#si el codigo es 3 se suma 1 a el acumulador de alimentos
	elif codigo==3:
		alimentos+=1
#si el codigo no es uno de los anteriores se muestra un mensaje de invalidacion
	else:
		print("Código inválido")
#se muestra el porcentaje que ocupa cada categoria 
print(f"Electrónica: {electronica} artículos --> {electronica/N*100}%")
print(f"Ropa: {ropa} artículos --> {ropa/N*100}%")
print(f"Alimentos: {alimentos} artículos --> {alimentos/N*100}%")
#se muestra el total de articulos registrados
print(f"Total de artículos: {N}") 