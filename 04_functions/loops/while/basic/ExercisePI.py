'''Pide al usuario un número entero positivo N, 
y muestra los números del 1 al N uno por uno.'''

class Numero():

    def __init__(self):
        self.numero = 0

    def pedir_numero(self):
        while True:
            try: #Intenta ejecutar este bloque de codigo
                self.numero = int(input("Ingrese un numero entero positivo: "))
                if self.numero > 0:
                    break
                else:
                    print("El numero debe de ser mayor a 0")

            except ValueError: #En el caso que no, muestra el siguiente error
                print("Por favor, ingrese un numero entero valido")

    def mostrar_numeros(self):
        for i in range(1,self.numero + 1):
            print(i)

call = Numero()

call.pedir_numero()
call.mostrar_numeros()