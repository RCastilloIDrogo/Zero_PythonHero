texto = "Hola Mundo"
print(texto.upper()) #upper convierte toda la variable de texto en MAYUS
print(texto.lower())
print(texto.find("Mun"))
print(texto.find("mun"))
nuevoTexto = print(texto.replace("Mun" , "chanchito feliz"))

print(texto, nuevoTexto)
print("Mundo" in texto)