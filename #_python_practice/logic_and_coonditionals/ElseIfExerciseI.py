calificacion = float(input("Ingrese la calificación del estudiante: "))

if calificacion >= 100:
    print("Excelente!")
elif calificacion >= 80:
    print("Sobresaliente")
elif calificacion >= 50:
    print("Regular")
elif calificacion >= 20:
    print("Bajo")
elif calificacion >= 0:
    print("Reprobado")
else:
    print("Ingrese un numero como calificación!")