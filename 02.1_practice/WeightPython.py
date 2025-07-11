import tkinter as tk
from tkinter import simpledialog, messagebox
import string

root = tk.Tk()
root.withdraw() #Evitar que se muestre la interfaz

#Preguntar cuanto pesa el usuario

wh = simpledialog.askfloat("Peso",
                            "Cual es tu peso a la fecha, sin mentir papai:")

if wh and wh > 0:
    if wh > 90:
        messagebox.showinfo("Alerta de Peso", f"Tu peso es {wh}kg.\n¡Ojo! Estás pasadito de peso.")
    else:
        messagebox.showinfo("Buen peso", f"Tu peso es {wh} kg.\n¡Estás en buen peso, sigue así!")
else:
    messagebox.showerror("Error", "Por favor ingresa un valor válido mayor que 0.")
