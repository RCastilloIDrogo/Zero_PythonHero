'''Pide al usuario que ingrese una contraseña.
Sigue pidiendo hasta que la escriba correctamente.
Solo se detiene si escribe "python123".'''


class ContraseñaCorrecta():

    def __init__(self):
        self.correcta = 'dungaunga'

    def validar(self):
        intento = ''

        while intento != self.correcta:
            intento = input("Escribe la contraseña: ")
            if intento != self.correcta:
                print("Contraseña Incorrecta")

        print("Contraseña Correcta!!!!")

call = ContraseñaCorrecta()

call.validar()