'''Estás programando un sistema para registrar el peso de paquetes que llegan a una bodega. 
Se pide el peso de cada paquete hasta que se ingrese 0. Al final se muestra cuántos paquetes 
se registraron y el peso total.

Pistas:
Usa un contador (paquetes) y un acumulador (peso_total).
Usa while hasta que se ingrese 0.
Incrementa el contador en cada vuelta.'''

class RegistroPaquetes:
    def __init__(self):
        self.peso = 0
        self.contador_paquetes = 0
        self.peso_total = 0

    def pedir_peso(self):
        self.peso = float(input("Podría ingresar el peso del paquete, por favor (0 para terminar): "))

        while self.peso != 0:
            self.contador_paquetes += 1
            self.peso_total += self.peso
            self.peso = float(input("Ingrese el siguiente peso (0 para terminar): "))

        print("Total de paquetes registrados:", self.contador_paquetes)
        print("Peso total:", self.peso_total)

# Uso
call = RegistroPaquetes()
call.pedir_peso()
