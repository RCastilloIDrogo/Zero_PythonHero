'''Pide al usuario 5 números uno por uno.
Al final, muestra cuál fue el número más grande ingresado.'''

class Numeros():

    def __init__(self):
        self.numero = []

    def pedir_numeros(self):
        while len(self.numero) < 5:
            try:
                numero = int(input("Ingrese un numero positivo: "))

                if numero == 12:
                    while True:
                        decision = input(f"El numero {numero} no esta permitido, ¿Desea cambiarlos? (S/N)").lower()
                        if decision == 's':
                            break
                        elif decision == 'n':
                            print("El numero no fue procesado. El programa termina.")
                            return
                        else:
                            print("Respuesta invalidad. Ingrese 'S' o 'N'.")
                    continue
                if numero < 0:
                    print("Solo se permiten numero positivos.")
                    continue

                self.numero.append(numero)
                print("Numero valido")

            except ValueError:
                print("Entrada invalida. Debe ser un numero entero")

    def mostrar_mayor(self):
        if self.numero:
            print("El numero mas grande ingresado es", max(self.numero))
        else:
            print("No se ingresaron numero validos")

call = Numeros()

call.pedir_numeros()
call.mostrar_mayor()