import tkinter as tk
from tkinter import simpledialog, messagebox


root = tk.Tk()
root.withdraw()

edad = simpledialog.askfloat("Edad", "¿Cuantos años tienes?")

if edad and edad > 0:
    if edad < 13:
        messagebox.showinfo("Edad", "Eres solo un niño!")
    elif edad < 16:
        messagebox.showinfo("Edad", "Aun eres demasiado Joven")
    elif edad < 18:
        messagebox.showinfo("Edad", "Ya eres mayor de edad!")
    elif edad < 22:
        messagebox.showinfo("Edad", "Es hora de chambear")

else:
    messagebox.showerror("Error", "Por favor,  ingresa una edad valida")