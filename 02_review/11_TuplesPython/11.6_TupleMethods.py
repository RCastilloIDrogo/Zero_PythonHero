'''Ahora mismo vamos a ver algo breve con los metodos que se utilizan dentro de una tuple
en este caso por lo visto son 2 en base a lo revisado y son los siguientes:'''

#count() | Devuelve el numero de veces que ocurre un valor especifico en la tuple
#index() | Busca un valor especifico en la tuple y devuelve la posicion de donde se encontro

#Bueno basicamente el primer metodo sirve de la siguiente forma

temp = ("Ropa", "Adornos", "Papa Noel", "GreenDay","Ropa","Ropa","Ropa")
cantidad = temp.count("Ropa")
indicevalor = temp.index("Papa Noel")

print("Esta es la cantidad del valor repetido: ",cantidad)
print("Este es indice del valor seleccionado: ", indicevalor)