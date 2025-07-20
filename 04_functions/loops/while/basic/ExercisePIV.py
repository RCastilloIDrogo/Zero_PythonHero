'''El usuario debe escribir el PIN correcto (por ejemplo, "4321"). Si se equivoca, 
puede intentarlo otra vez. El programa sigue pidiendo el PIN hasta que lo acierte.'''

class PinPassword:

    def __init__(self):
        self.pin = '4321'

    def pedir_pin(self):
        while True:
            pin = input("Ingrese el PIN correcto: ")
            if pin == self.pin:
                print("PIN correcto. Acceso concedido.")
                break
            else:
                print("PIN incorrecto. Inténtelo nuevamente.")

# Uso
call = PinPassword()
call.pedir_pin()