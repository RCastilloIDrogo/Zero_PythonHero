import tkinter as tk
from tkinter import messagebox, simpledialog

# Necesitas crear la raíz de la ventana (aunque no la muestres)
root = tk.Tk()
root.withdraw()  # Oculta la ventana principal

messagebox.showinfo("Título", "Hola Mundo")
