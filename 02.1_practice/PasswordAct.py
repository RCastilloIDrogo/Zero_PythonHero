import tkinter as tk
from tkinter import simpledialog, messagebox
import string, random

root = tk.Tk()
root.withdraw()

# Preguntar al usuario la longitud de la contraseña
long = simpledialog.askinteger("Longitud", 
        "¿Cuántos caracteres quieres que tenga tu contraseña?")

if long and long > 0:
    # Conjunto de caracteres a usar
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Generar la contraseña
    contraseña = ''.join(random.choice(caracteres) for _ in range(long))

    # Mostrar la contraseña generada
    messagebox.showinfo("Contraseña Generada", 
    f"Tu contraseña es:\n{contraseña}")
else:
    messagebox.showerror("Error", 
    "Debes ingresar un número válido mayor que 0.")
