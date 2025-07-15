num = int(input("Cuantos numeros naturales quieres sumar: "))

suma = 0

for item in range(1, num + 1):
    suma += item

print("Las suma es: ", suma)