"""
Repaso-Problema2
Una empresa que contrata personal requiere determinar la edad de las personas que solicitan trabajo, pero cuando
se les entrevista sólo se les pregunta el año en que nacieron.
"""
año_actual=2026
"""se pone valor al año actual"""
año_nacimiento=int(input("Ingrese su año de nacimiento"))
"""Se pide el año de nacimiento"""
edad=año_actual - año_nacimiento
"""se hace la operación para obtener la edad"""
print(f"SU edad es {edad}")
"""Se imprime la edad"""