#Ahora mismo lo que vamos a estar practicando es el uso de cadenas
#Haciendo uso de las misma dentro de una clase con sus respectivas funciones

class ProcesadorTexto():

    def __init__(self):
        self.texto = ''

    def pedir_texto(self):
        self.texto = input("Ingresa un Texto: ")

    def mostrar_minusculas(self):
        return self.texto.lower()
    
    def contar_letras(self):
        return len(self.texto)
    
#Creamos un objeto de la misma clase
call = ProcesadorTexto()

call.pedir_texto()
minusculas = call.mostrar_minusculas()
conteo = call.contar_letras()

print("Texto en minusculas: ", minusculas)
print("Conteo de Letras: ", conteo)