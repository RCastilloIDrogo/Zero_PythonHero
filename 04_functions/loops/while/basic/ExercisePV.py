'''Entra una persona a una sala y se pregunta su nombre. Si el usuario escribe "fin", 
termina el conteo. Al final se muestra cuántas personas ingresaron.'''

class SalaPersonas():

    def __init__(self):
        self.persona = []

    def pedir_nombre(self):

        while True:
            nombre = input("Ingrese el nombre de la persona (o fin para terminar): ")
            if nombre.lower() ==  'fin':
                break

            self.persona.append(nombre)

    def mostrar_total(self):
        print("Personas ingresadas:", self.persona)
        print("Cantidad de personas que ingresaron:", len(self.persona))


call = SalaPersonas()

call.pedir_nombre()
call.mostrar_total()