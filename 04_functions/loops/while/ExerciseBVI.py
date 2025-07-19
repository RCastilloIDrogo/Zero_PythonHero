'''Estás programando el sistema de ingreso de autos a un estacionamiento. El vigilante debe ingresar la placa de cada vehículo que entra. 
El proceso se repite hasta que el vigilante escriba "SALIR" (en mayúsculas).

Al final, el sistema debe mostrar:

Cuántos vehículos ingresaron.
La lista de placas ingresadas.'''

class Estacionamiento():

    def __init__(self):
        self.placa = ''
        self.auto = ''
