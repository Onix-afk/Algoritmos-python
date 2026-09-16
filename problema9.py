"""
Determina el promedio que obtendrá un alumno considerando que realiza tres exámenes,
de los cuales el primero y el segundo tienen una ponderación de 25%, mientras que el
tercero de 50%
"""
"""Se piden tres calificaciones"""
cal1=float(input("Ingresa la primera calificacion"))
cal2=float(input("Ingresa la segunda calificacion"))
cal3=float(input("Ingresa la tercera calificacion"))
"""Se ponen porcentajes a cada calificación"""
cali1=cal1*0.25
cali2=cal2*0.25
cali3=cal3*0.5
"""Se calcula el promedio"""
promedio=cali1+cali2+cali3
"""Se muestra el resultado"""
print(f"tu promedio es: {promedio}")