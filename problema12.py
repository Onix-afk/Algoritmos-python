"""
"La langosta ahumada" es una empresa dedicada a ofrecer banquetes;
sus tarifas son las siguientes: el costo de platillo por persona es 
de $95.00, pero si el número de personas es mayor a 200 pero menor
o igual a 300, el costo es de $85.00. Para más de 300 personas el 
costo por platillo es de $75.00. Se requiere un algoritmo que ayude 
a determinar el presupuesto que se debe presentar a los clientes que
deseen realizar un evento.
"""
"""Se pide el numero de personas que van a comer"""
per=int(input("Cuantas personas van a comer: "))
"""si hay entre 201 y 300 personas el platillo cuesta $85"""
if(per>200 and per==300):
	pago=per*85.00
"""si hay mas de 300 personas el platillo cuesta $75"""
elif(per>300):
	pago=per*75.00
"""si hay 200 personas o menos el platillo cuesta $95"""
else:
	pago=per*95.00
"""Se muestra el total a pagar"""
print(f"va a pagar: ${pago}")