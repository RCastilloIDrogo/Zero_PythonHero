'''El sistema tiene un número secreto (por ejemplo, 23).
El usuario debe adivinarlo.
Después de cada intento, el programa dice si el número es mayor o menor que el secreto.
Repite hasta que lo adivine.'''

import random

class NumeroSecreto():

    def __init__(self):
        self.numero = 0