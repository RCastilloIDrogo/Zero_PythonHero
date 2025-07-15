#Crea una clase CalculadoraBasica con un método llamado operacion_total.
#El método debe pedir tres números al usuario (n1, n2, n3)
#Retornar el resultado de: (n1 + n2) \times n3

class CalculadoraBasica():

    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0

    def operacional_total(self):
        self.n1 = float(input("Ingrese el valor de n1: "))
        self.n2 = float(input("Ingrese el valor de n2: "))
        self.n3 = float(input("Ingrese el valor de n3: "))
        
        return (self.n1 + self.n2) * self.n3
    
#Creamos un objeto de la misma clase
call = CalculadoraBasica()
resultado = call.operacional_total()

print("El resultado de la operacion es:" , resultado)