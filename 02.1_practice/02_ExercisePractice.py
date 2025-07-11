

class Verificador:
    def __init__(self, edad, numero):
        self.edad = edad
        self.numero = numero

    def verificar_edad(self):
        if self.edad >= 18:
            return f"Tienes {self.edad} años: Eres mayor de Edad"
        else:
            return f"Tienes {self.edad} años: Aún eres menor de Edad"
        
    def verificar_paridad(self):
        if self.numero % 2 == 0:
            return f"El numero {self.numero} es par"
        else:
            return f"El numero {self.numero} es impar"
        
verificarEdad = int(input("Ingrese su edad mi estimado cpp: "))
verificar_par = int(input("Ingrese el numero a verificar su paridad: "))

#Importante! Se debe de crear el objeto

verificador = Verificador(verificarEdad, verificar_par)

print(verificador.verificar_edad())
print(verificador.verificar_paridad())

