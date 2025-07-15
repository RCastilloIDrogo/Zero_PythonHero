#Pide una palabra y cuenta cuántas vocales tiene

palabra = input("Ingrese una palabra: ")

contador_vocals = 0

for letra in palabra:
    if letra.lower() in 'aeiou':
        contador_vocals += 1

print("La palabra tiene", contador_vocals, "vocales")