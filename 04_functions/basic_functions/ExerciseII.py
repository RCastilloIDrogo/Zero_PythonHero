#Ahora mismo lo que vamos hacer es un pequeño repaso con respecto a "self" 
#Para entender de mejor manera el uso

#Crear una clase Persona que tenga un atributo nombre, y un método saludar() que
#diga "Hola, soy [nombre]".

class Persona():
    def __init__(self):
        self.nombre = ""

    def pedir_nombre(self):
        self.nombre = input("Cual es tu nombre? ")

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

call = Persona()

call.pedir_nombre()
call.saludar()