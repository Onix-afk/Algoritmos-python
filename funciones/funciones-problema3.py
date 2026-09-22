"""
Diseña una función llamada repetir_texto(texto,veces) que 
devuelva la palabra repetida la cantidad de veces indicada.
-Prueba1:repetir_texto("Eco",3)"EcoEcoEco"
-Prueba2:repetir_texto("Hola",1)"Hola"
-Prueba3:repetir_texto("Ja",4)"JaJaJaJa"
"""
#se toma un texto y se repite la cantidad de veces indicada
def repetir_texto(texto, veces):
	return texto*veces
#se muestran resultados
print(repetir_texto("Eco",3))
print(repetir_texto("Hola",1))
print(repetir_texto("Ja",4))