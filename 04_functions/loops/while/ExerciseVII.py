'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
todos los años que ha cumplido (desde 1 hasta su edad).'''
import time

class PreguntaEdad():

    def __init__(self):
        self.edad = ''

    def solicitar_edad(self):
        self.edad = int(input("Ingrese su edad: "))

    def mostrar_edad(self):
        i = 1
        while i != self.edad:
            time.sleep(0.5)
            print("Has cumplido: {} años".format(i))
            i += 1

call = PreguntaEdad()

call.solicitar_edad()
call.mostrar_edad()