"""
Crea una función llamada saludar(nombre) que recibe un nombre
como cadena de texto y retorne "Hola, <nombre>!"
-Prueba1:saludar("Carlos"):"Hola, Carlos!" 
-Prueba2:saludar("Ana"):"Hola, Ana!" 
-Prueba3:saludar("Mundo"):"Hola, Mundo!"
"""
#recibe el nombre y regresa un saludo
def saludar(nombre):
#se crea el mensaje de saludo con el nombre recibido
	return f"Hola,{nombre}!"
#se muestra el resultado
print(saludar("Carlos"))
print(saludar("Ana")) 
print(saludar("Mundo")) 