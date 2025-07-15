#Crea una clase EditorTexto que tenga los siguientes métodos:
# pedir_texto(): pide al usuario un texto y lo guarda en un atributo
# limpiar(): devuelve el texto sin espacios al inicio y al final
# todo_mayusculas(): devuelve el texto en mayúsculas
# contar_palabras(): devuelve la cantidad de palabras (usa split() y len())

class EditorTexto():

    def __init__(self):
        self.texto = ''

    def pedir_texto(self):
        self.texto = input("Ingrese el texto: ")

    def limpiar(self):
        #Elimina los espacios al inicio y al final
        return self.texto.strip() 

    def todo_mayusculas(self):
        #Devuelve todo el texto ingresado en mayusculas
        return self.texto.upper()

    def contar_palabras(self):
        #Divide el texto con split()
        palabras = self.texto.split()
        #Cuenta con len()
        return len(palabras)
    
call = EditorTexto()

call.pedir_texto()
clean = print("Este es el texto sin espacios: ",call.limpiar())
mayusculas = print("Texto todo en mayusculas: ", call.todo_mayusculas())
conteo = print("Conteo de palabras: ", call.contar_palabras())