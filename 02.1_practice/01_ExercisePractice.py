import tkinter as tk
from tkinter import messagebox, simpledialog

class Calculadora:
    def __init__(self, num1, num2): #Inicializa | Al crear un nuevo objeto
        self.num1 = num1 #self | Se refiere al objeto actual, es como decir "Yo mismo"
        self.num2 = num2
    
    def sumar(self):
        return self.num1 + self.num2
    def restar(self):
        return self.num1 - self.num2
    def multiplicar(self):
        return self.num1 * self.num2
    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: División entre cero"

n1 = simpledialog.askfloat("Variable", "Ingrese el numero para la variable I: ")
n2 = simpledialog.askfloat("Variable", "Ingrese el numero para la variable II: ")
operacion = simpledialog.askstring("Operacion","¿Qué operación quieres hacer? (sumar, restar, multiplicar, dividir): ")
#Creamos el Objeto
calc = Calculadora(n1, n2)

#Ahora vamos hacer la logica como tal haciendo llamdo de las funciones definidas en las clase

if operacion == "sumar":
    resultado = calc.sumar()

elif operacion == "restar":
    resultado = calc.restar()
elif operacion == "multiplicar":
    resultado = calc.restar()
elif operacion == "division":
    resultado = calc.restar()

else:
    resultado = messagebox.showerror("Error", "Operación no válida")

messagebox.showinfo("Resultado", resultado)