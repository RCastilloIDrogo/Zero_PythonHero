'''Ahora mismo lo que vamos hacer es un conteo de un numero pero ingresado
por el mismo usuario'''

import time
class ConteoNumero():

    def __init__(self):
        self.num = 0

    def pedir_numero(self):
        self.numero = int(input("Ingrese su numero: "))

    def conteo_n(self):
        i = 0

        while self.numero != 0:
            time.sleep(1)
            print(i)
            i += 1

call = ConteoNumero()

call.pedir_numero()
call.conteo_n()