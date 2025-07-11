class Numeros:
    def __init__(self):
        pass
    
    def imprimir_cadena(self):
        print("Numeros del 1 al 200")
        for item in range (1, 201):
            print(item)

    def sumar_multiplos(self):
        suma = 0
        for item in range(1, 51):
            if item % 3 == 0:
                suma += item
        return suma
    
#Creamos el objeto

numeros = Numeros()

numeros.imprimir_cadena()
resultado_suma = numeros.sumar_multiplos()

print("La suma de los multiplos de 3 entre 1 y 50 es: ", resultado_suma)