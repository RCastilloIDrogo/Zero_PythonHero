#Pide números al usuario mientras no ingrese un número negativo.
# Al final, muestra la suma total de todos los números ingresados 
# (sin contar el negativo).

class SumaPositivos:
    def __init__(self):
        self.total = 0

    def ejecutar(self):
        numero = 0
        while numero >= 0:
            numero = int(input("Ingresa un número positivo (negativo para salir): "))
            if numero >= 0:
                self.total += numero
        print(f"Suma total: {self.total}")

# Uso
suma = SumaPositivos()
suma.ejecutar()
