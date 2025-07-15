#Que es un parametro? | Variable definia en la funcion donde recibe un valor cuando se llama
#Ojo! Este valor es unico y local para la funcion

class Baby():
    
    def __init__(self):
        self.name = ""
        self.edad = 0

    def pedir_datos(self):
        self.edad = int(input("Cuantos años tienes?: "))
        self.name = input("Cual es tu nombre?: ")
    
    def mostrar_edad(self):
        print("=" * 40)
        if self.edad < 10:
            print("Eres juvenil")
        elif 10 <= self.edad < 18:
            print("Aun no puedes votar")
        elif self.edad >= 18:
            print("Eres mayor de edad")

    
    def edad_par(self):
        print("=" * 40)
        if self.edad % 2 == 0:
            print(f"{self.edad} es par")
        else:
            print(f"{self.edad} es impar")
    
    def mostrar_datos(self):
        print("=" * 40)
        print(f"Tu nombre es {self.name} y tienes {self.edad} años")
            
#Creamos el objeto
call = Baby()

#Hacemos el llamado de la funciones declaradas
call.pedir_datos()
call.edad_par()
call.mostrar_datos()