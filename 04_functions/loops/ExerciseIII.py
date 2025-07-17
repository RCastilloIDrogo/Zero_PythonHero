#Crea una clase llamada ValidadorNumero. Debe hacer lo siguiente:
# Pedir al usuario un número usando input() o simpledialog

# Si el número ingresado es negativo, mostrar un mensaje de error y repetir 
# hasta que se ingrese un número positivo

# Cuando se ingrese un número válido, mostrar: "Número aceptado: X"

import tkinter as tk
from tkinter import messagebox, simpledialog

class ValidadorNumero:
    def __init__(self):
        self.numero = 0

    def pedir_numero(self):
        while True:
            try:
                self.numero = simpledialog.askinteger("Valor N", "Ingrese un número positivo:")
                
                # Verifica si el usuario cerró la ventana
                if self.numero is None:
                    messagebox.showwarning("Cancelado", "No ingresaste ningún número.")
                    return

                # Validación: número debe ser mayor a 0
                if self.numero > 0:
                    break
                else:
                    messagebox.showerror("Error", "El número debe ser mayor a cero.")
            
            except ValueError:
                messagebox.showerror("Error", "Entrada inválida. Intente de nuevo.")

        messagebox.showinfo("Éxito", f"Número aceptado: {self.numero}")

root = tk.Tk()
root.withdraw()

validador = ValidadorNumero()
validador.pedir_numero()
