'''Pide al usuario que escriba la palabra mágica "python". Si escribe otra cosa, 
vuelve a pedirlo hasta que escriba la palabra correcta.'''

class PalabraSecreta():

    def __init__(self):
        self.password = 'python'
        self.intentos_max = 3

    def pedir_password(self):
        intentos = 0

        while intentos < self.intentos_max:
            contraseña = input("Escriba la palabra magica: ")
            if contraseña.lower() == self.password:
                print("Contraseña Correcta!")
                return
            else:
                intentos += 1
                print(f"Contraseña incorrecta. Intento {intentos} de {self.intentos_max}")
        print("Has superado el numero maximo de intentos")

call = PalabraSecreta()

call.pedir_password()