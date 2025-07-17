#Contar del 1 al numero ingresado

class Contador():

    def __init__(self):
        self.numero = 0

    def pedir_numero(self):
        self.numero = int(input("Ingrese un numero positivo"))

    def contar(self):
        i = 1
        while i <= self.numero:
            print(i)
            i += 1

call = Contador()

call.pedir_numero()
call.contar()