#Crea una clase llamada TextoAnalizado con las siguientes características:
# pedir_texto(): pide al usuario un texto y lo guarda.
# mostrar_estadisticas(): muestra cuántas veces aparece cada vocal (a, e, i, o, u).
# palabras_largas(minimo): retorna una lista con las palabras que tienen más de minimo letras.
# contiene_palabra(clave): retorna True si la palabra clave existe en el texto
# sin importar mayúsculas/minúsculas.

import tkinter as tk
from tkinter import messagebox, simpledialog

class TextoAnalizado():
    
    def __init__(self):
        self.texto = ''

    def pedir_texto(self):
        self.texto = simpledialog.askstring("Texto", "Ingrese el Texto: ")
    
    def mostrar_estadisticas(self):
        vocales = 'aeiou'
        conteo = {vocal: 0 for vocal in vocales} #Se crea un diccionario

        for letra in self.texto.lower():
            if letra in vocales:
                conteo[letra] += 1
        
        messagebox.showinfo("Mensaje", "Estadisticas de Vocales: ")
        for vocal, cantidad in conteo.items():
            messagebox.showinfo("Dicionario", f"{vocal}: {cantidad}")

    def palabras_largas(self, minimo):
        palabras = self.texto.split()
        largas = []

        for palabra in palabras:
            # Elimina los signos de puntuacion, si es que lo hay
            palabra_limpia = palabra.strip(".,;:!?")

            if len(palabra_limpia) > minimo:
                largas.append(palabra_limpia)

        return largas
    
    def contiene_palabra(self, clave):
        palabras = self.texto.lower().split()
        return clave.lower() in [palabra.strip(".,;:!?") for palabra in palabras]
    
root = tk.Tk()
root.withdraw()

texto = TextoAnalizado()
texto.pedir_texto()

texto.mostrar_estadisticas()

minimo = int(input("\n¿Palabras con más de cuántas letras?: "))
print("Palabras largas:", texto.palabras_largas(minimo))

clave = input("\n¿Palabra a buscar?: ")
if texto.contiene_palabra(clave):
    print(f"La palabra '{clave}' está presente en el texto.")
else:
    print(f"La palabra '{clave}' no se encuentra en el texto.")
