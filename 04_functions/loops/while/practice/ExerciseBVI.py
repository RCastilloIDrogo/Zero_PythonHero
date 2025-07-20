'''Estás programando el sistema de ingreso de autos a un estacionamiento. El vigilante debe ingresar la placa de cada vehículo que entra. 
El proceso se repite hasta que el vigilante escriba "SALIR" (en mayúsculas).

Al final, el sistema debe mostrar:

Cuántos vehículos ingresaron.
La lista de placas ingresadas.'''

class Estacionamiento():

    def __init__(self):
        self.placa = []

    def ingreso_autos(self):

        while True:
            placa = input("Ingrese la placa del auto (o 'SALIR' para terminar): ").upper()

            if placa == "SALIR":
                break

            if placa == "":
                print("Placa vacia no permitida")
                continue

            self.placa.append(placa)
        
        print("Total de vehiculos ingresados", len(self.placa))
        print("Lista de Placas:")
        
        for p in self.placa:
            print("-", p)

call = Estacionamiento()

call.ingreso_autos()
