'''El programa tiene un número secreto (por ejemplo, 7).
El usuario debe adivinarlo.
Si acierta, muestra "Correcto".
Si no, sigue intentando.'''

import random

class AdivinaConPistas:
    def __init__(self):
        self.secreto = random.randint(1, 20)

    def jugar(self):
        intento = None
        print("🎲 Adivina un número entre 1 y 20")

        while intento != self.secreto:
            intento = int(input("Tu intento: "))

            if intento == self.secreto:
                print("¡Correcto! El número era", self.secreto)
            elif abs(intento - self.secreto) <= 3:
                print("¡Estás cerca!")
            elif intento > self.secreto:
                print("Muy alto")
            else:
                print("Muy bajo")

# Uso
juego = AdivinaConPistas()
juego.jugar()
