"""
Almacenes "El harapiento distinguido" tiene una promoción: a todos los trajes que tienen un precio
superior a $2500.00 se les aplicará un descuento de 15% a todos los demás se les aplicará sólo 8%.
Realice un algoritmo para determinar el precio final que debe pagar una persona por comprar un traje
 y de cuánto es el descuento que obtendrá.
"""
"""Se pide el precio del traje"""
precio=float(input("Ingresa el precio del traje: $"))
"""se verifica si aplica el descuento mayor"""
if precio > 2500:
	descuento_porcentaje=15
else:
	descuento_porcentaje=8
"""se calcula el monto del descuento y el precio final"""
descuento=precio*(descuento_porcentaje/100)
precio_total=precio-descuento
"""se muestran los resultados"""
print(f"Descuento aplicado: {descuento_porcentaje}%")
print(f"Monto del descuento: {descuento}")
print(f"El total a pagar es: {precio_total}")