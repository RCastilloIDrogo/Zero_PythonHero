'''Pide al usuario un número positivo, y cuenta desde 
ese número hasta 0 mostrando uno por uno.'''

import time

class NumeroPositivo():

    def __init__(self):
        self.numero = 0

    def pedir_numero(self):
        while True:
            try:
                self.numero = int(input("Ingrese un numero positivo: "))
                if self.numero > 0:
                    break
                else:
                    print("Ingrese un numero positivo")
            except ValueError:
                print("Ingrese un numero valido")
        
    def mostrar_numero(self):
        i = self.numero
        while i >= 0:
            time.sleep(1)
            print(i)
            i -= 1

call = NumeroPositivo()

call.pedir_numero()
call.mostrar_numero()