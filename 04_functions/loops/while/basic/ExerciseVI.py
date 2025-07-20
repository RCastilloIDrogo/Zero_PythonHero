'''Escribir un programa que pida un numero al usuario y 
muestre las tablas de multiplicar de ese numero'''

class Operacion():

    def __init__(self):
        self.numero = 0

    def pedir_numero(self):
        self.numero = int(input("Ingrese su numero: "))
    
    def tabla_multiplicar(self):
        
        i = 0
        multi = 0
        while i <= 12:
            multi = self.numero * i
            print("{} x {} = {}".format(self.numero, i, multi))
            i += 1

call = Operacion()

call.pedir_numero()
call.tabla_multiplicar()

