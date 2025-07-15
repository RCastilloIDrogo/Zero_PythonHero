#Crea un programa que defina una clase llamada Operaciones, la cual debe permitir 
#realizar varias funciones matemáticas básicas

# Calcular el área de un rectángulo a partir de una base y una altura.
# Obtener el cuadrado de un número dado.
# Determinar si una persona es mayor de edad según su edad.
# Sumar todos los elementos de una lista de números.


class Triangulo():
    def __init__(self):
        self.base = 0
        self.altura = 0
        #self.figuras = 0
    
    def datos_triangulo(self):
        self.base = float(input("Ingrese la base del triangulo: "))
        self.altura = float(input("Ingrese la altura del triangulo: "))

    def area_triangulo(self):
        return (self.base * self.altura) / 2
    

class Operaciones():

    def __init__(self):
        self.numero = 0
        self.edad = 0
    
    def definir_datos(self):
        self.numero = float(input("Ingrese un numero: "))
        self.edad = int(input("Ingrese su edad: "))

    def cuadrado_n(self):
        return self.numero ** 2
    
    def mayor_edad(self):
        return self.edad >= 18

#Declarar objeto para la clase Triangulo
tr = Triangulo()

#Llamado de las funciones de la clase Triangulo
tr.datos_triangulo()
print("Area del Triangulo: ",tr.area_triangulo())

#Declarar objeto para la clase Operaciones
op = Operaciones()

#Llamado de las funciones de la clase Triangulo
op.definir_datos()
print("El cuadro del numero es", op.cuadrado_n())

if op.mayor_edad():
    print("Es mayor de Edad")
else:
    print("Es menor de Edad")