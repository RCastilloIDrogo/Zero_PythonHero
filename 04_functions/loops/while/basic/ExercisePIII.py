'''Pide al usuario que ingrese números. Suma todos hasta que 
escriba 0. Luego muestra el total.'''

class UsuarioNumero():

    def __init__(self):
        self.numero = []

    def pedir_numeros(self):
        while True:
            try:
                numero = int(input("Ingrese un numero: "))
                if numero == 0:
                    break
                self.numero.append(numero)
            
            except ValueError:
                print("Ingrese un valor correcto!")

    def mostrar_resultados(self):
        print("Numeros ingresados: ", self.numero)
        print("La suma total es: ", sum(self.numero))

call = UsuarioNumero()

call.pedir_numeros()
call.mostrar_resultados()