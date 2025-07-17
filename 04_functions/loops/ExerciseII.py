#Este es un ejemplo del uso del while en una clase

class ContadorRegresivo():

    def __init__(self):
        self.numero = 0

    def pedir_numero(self):
        try:
            self.numero = int(input("Ingrese un numero entero positivo: "))

        except ValueError:
            print("Numero invalido. Usando 0 por defecto")
            self.numero = 0

    def contar_regresivo(self):
        if self.numero <= 0:
            print("No se puede contar desde cero a numero negativo")
            return
        
        print("\nContando regresivamente:")
        while self.numero > 0:
            print(self.numero)
            self.numero -= 1
        print("¡Despegue!")

call = ContadorRegresivo()

call.pedir_numero()
call.contar_regresivo()