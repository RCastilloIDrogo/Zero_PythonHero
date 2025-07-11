import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import subprocess

# Configurar ventana oculta
root = tk.Tk()
root.withdraw()

# Pedir peso
peso = simpledialog.askfloat("Peso", "¿Cuál es tu peso en kilogramos?")

# Si es saludable (< 80), mostrar imagen
if peso < 80:
    ventana = tk.Toplevel()
    ventana.title("¡Estás saludable!")
    ventana.geometry("400x400")
    
    # Cargar imagen
    img = Image.open("happy.png")  # Usa tu imagen
    img = img.resize((280, 280))
    foto = ImageTk.PhotoImage(img)

    label = tk.Label(ventana, image=foto)
    label.pack()

    texto = tk.Label(ventana, text="¡Sigue así! 💪")
    texto.pack()

    ventana.mainloop()

else:
    # Mostrar mensaje y abrir video externo
    messagebox.showinfo("Atención", "Necesitas cuidar tu salud. Reproduciendo video...")
    
    # Abrir video con el reproductor del sistema
    subprocess.Popen(["start", "alerta_sobrepeso.mp4"], shell=True)  # En Windows
