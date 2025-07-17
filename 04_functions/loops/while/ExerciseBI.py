#Contar del 1 al 10
#Para hacerlo mas interesante vamos hacer uso de la libreria "time"

import time

class Conteo():

    def __init__(self):
        self.num = 0

    def count_1_10(self):
        i = 0

        while i <= 10:
            time.sleep(0.9)
            print(i)
            i += 1

#Declaramos un objeto de la clase

call = Conteo()

call.count_1_10()