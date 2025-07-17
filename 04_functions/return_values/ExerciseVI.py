#Crea una clase llamada AnalizadorTexto con los siguientes métodos:
# pedir_frase(): pide una frase al usuario y la guarda
# contar_vocales(): retorna cuántas vocales hay en total
# invertir_texto(): retorna el texto al revés
# es_palindromo(): retorna True si la frase es un palíndromo (ignora mayúsculas y espacios)

import tkinter as tk
from tkinter import messagebox, simpledialog

class AnalizadorTexto():

    def __init__(self):
        self.frase = ''

    def pedir_frase(self):
        self.frase = simpledialog.askstring("Frase", "Ingrese una frase:")

    def contar_vocales(self):
        frase = self.frase.lower()
        count = 0
        for letra in frase:
            if letra in 'aeiou':
                count += 1
        return count
    
    def invertir_texto(self):
        return self.frase[::-1]
    
    def es_palindromo(self):
        frase_limpia = self.frase.lower().replace(" ", "")# minúsculas y sin espacios
        return frase_limpia == frase_limpia[::-1]

root = tk.Tk()
root.withdraw()

call = AnalizadorTexto()
call.pedir_frase()
messagebox.showinfo("Conteo",f"Esta es la cantidad de vocales: {call.contar_vocales()}")
messagebox.showinfo("Invertir", f"Este es la frase invertidad: {call.invertir_texto()}")
messagebox.showinfo("Palindromo",f"La frase es palindromo?: {call.es_palindromo()}")