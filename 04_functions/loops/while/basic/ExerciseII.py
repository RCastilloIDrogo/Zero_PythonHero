import time

class CuentaRegresiva():

    def __init__(self):
        self.numero = 0

    def pedir_numero(self):
        self.numero = int(input("Ingrese un numero: "))

    def contar(self):
        while self.numero > 0:
            print(self.numero)
            time.sleep(2)
            self.numero -= 1
        print("Despegar!")

call = CuentaRegresiva()

call.pedir_numero()
call.contar()