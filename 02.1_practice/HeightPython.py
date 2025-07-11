import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()

# Preguntar por la estatura del usuario
hg = simpledialog.askfloat("Altura", "¿Cuánto mides actualmente? (en metros)")

# Validar que se ingresó un número positivo
if hg and hg > 0:
    if hg < 1.50:
        messagebox.showinfo("Altura", f"Mides {hg} m\nEstás bajito.")
    elif hg <= 1.80:
        messagebox.showinfo("Altura", f"Mides {hg} m\nTienes una altura promedio.")
    else:
        messagebox.showinfo("Altura", f"Mides {hg} m\n¡Eres alto!")
else:
    messagebox.showerror("Error", "Ingresa tu altura correctamente (por ejemplo: 1.75)")
