import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()

#En este apartado lo que vamos a solicitar son las variables
v1 = simpledialog.askfloat("Entrada", "Ingrese el valor de la variable I")
v2 = simpledialog.askfloat("Entrada", "Ingrese el valor de la variable I")

#Pedir la operación a realizar

operacion = simpledialog.askstring(
    "Operación",
    "Que deseas hacer con los numero?\nEscribe: suma, resta, multiplicar o dividir"
)

resultado = None

if operacion == "suma":
    resultado = v1 * v2
elif operacion == "resta":
    resultado = v1 - v2
elif operacion == "multiplicar":
    resultado = v1 * v2
elif operacion == "dividir":
    if v2 != 0:
        resultado = v1 / v2
    else:
        messagebox.showerror("Error", "No se puede dividir entre 0")
else:
    messagebox.showerror("Error", "Operación no Valida")

if resultado is not None:
    messagebox.showinfo("Resultado", f"El resultado es : {resultado}")