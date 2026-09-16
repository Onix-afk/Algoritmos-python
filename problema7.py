"""
Determina cuánto pagará finalmente una persona por un articulo equis, considerando que tiene un descuento de 
20%, y debe pagar 15% de IVA(debe mostrar el precio con descuento y el precio final).
Crea un menú para que el usuario elija entre 2 productos y el que elija, despliegue el nombre de producto, precio,
precio con descuento y precio final.
"""
"""se define el nombre y precio de los producto"""
productos={
	1:{"nombre": "Camisa", "precio": 350.00},
	2:{"nombre": "Pantalón", "precio": 520.00}
}
"""se muestra el menu al usuario"""
print("=====MENÚ DE PRODUCTOS=====")
print("1.Camisa")
print("2.Pantalón")
opcion=int(input("Elige el número del producto: "))
"""se verifica si la opcion es valida"""
if opcion not in productos:
	print("Opción invalida")
else: 
"""Se obtienen los datos del producto seleccionado"""
	prod=productos[opcion]
	nombre=prod["nombre"]
	precio=prod["precio"]
"""Se calcula el descuento del 20%"""
    descuento=precio*0.20
    precio_descuento=precio-descuento
"""Se calcula el 15% de IVA sobre el precio con descuento"""
    iva=precio_descuento*0.15
    precio_final=precio_descuento+iva
"""Se muestran los resultados"""
print(f"Producto: {nombre}")
print(f"Precio original: ${precio}")
print(f"Descuento(20%): -${descuento}")
print(f"Precio con descuento: ${precio_descuento}")
print(f"IVA (15%): +${iva}")
print(f"Precio final: ${precio_final}")