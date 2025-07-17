#Ahora mismo lo que vamos a reaprender es el uso del "while" y "for" pero no de forma simple
#Sino haciendo uso de clases

#Contador del 1 al N
#Crea una clase llamada Contador. Esta debe tener un método que:
# Pida un número al usuario
# Use un bucle for para contar desde 1 hasta ese número, mostrando los valores uno a uno.

import tkinter as tk
from tkinter import messagebox, simpledialog

class Contador():

    def __init__(self):
        self.numero = 0
    
    def pedir_numero(self):
        try:
            self.numero = simpledialog.askinteger("N1", "Ingrese el valor del numero: ")
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un numero valido")
            self.numero = 0

    def contar_hasta(self):
        if self.numero == 0:
            return

        conteo = ""
        for item in range(1, self.numero + 1):
            conteo += str(item) + "\n"

        messagebox.showinfo("Conteo", conteo)



call = Contador()

call.pedir_numero()

call.contar_hasta()