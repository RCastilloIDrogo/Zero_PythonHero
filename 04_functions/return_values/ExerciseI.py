#Que es return? | "Es una instruccion" |Donde devuelve un valor hacia donde fue llamada
#Considerando que esta dentro de la misma funcion

#"Este es el resultado de esta función, tómalo y úsalo donde la función fue llamada."

class PruebaReturn():

    def __init__(self):
        pass
    
    def saludar(self):
        return "Hola"
    
mensaje = PruebaReturn()
print(mensaje.saludar())
