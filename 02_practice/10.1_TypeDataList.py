#Siguiendo con las listas en python, nosotros podemos definir diferentes tipos de datos dentro de una lista
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = [12.2 , 33.4, 56.2]
print("---- STR ----")
print(list1)

print("---- INT ----")
print(list2)

print("---- BOOLEAN ----")
print(list3)

print("---- FLOAT ----")
print(list4)

#Ademas como anteriormente vimos podemos mostrar el tipo de dato de la coleccion de forma individual
print("---- Imprimir Lista ----")
list5 = ["Gordon", 18, True, 40.34, 8j]
print(type(list5))

print("---- Imprimir TypeData - Invividual ----")
#Considerando que esto es un constructor creando un objeto del tipo list
thislist = list(("apple", "banana", "cherry"))
for item in thislist:
    print(type(item))

#En python hay diversas colecciones las cuales podemos usar en este caso son 4
print("---- LIST ----")
#En esta coleccion permite duplicados, es ordenada y puede cambiarse
frutas = ["banana", "banana", "mango", "palanca"]
print(frutas[0:])
frutas[3] = "Gordon Freeman"
frutas.append("Pepe") #Con estaq funcion podemos agregar un nuevo valor a la lista
print("Esta es la Listas de Frutas Act: ",frutas)

print("---- TUPLE ----")
#Esta tambien es ordenada, pero no se puede cambiar!
#Pero si permite duplicados
cordenadas = (90, 89, 123)
print(cordenadas[1])

print("Estas son las cordenadas tuple: ",cordenadas)

print("---- SET ----")
#No tienen orden, no son indexados y no permiten duplicados
#Pero si se puede agregar

colores = {"rojo", "celeste", "amarillo", "morado"}
colores.add("verde")
colores.discard("rojo")
print("Estos son los colores que tengo: ",colores)

print("---- DICTIONARY ----")
# Usa claves, ordenado, cambiable, no permite claves repetidas
persona = {
    "nombre": "Carlos",
    "edad": 89,
    "ciudad": "Madrid"
}
print(persona["nombre"])   # Accede por clave → "Carlos"
persona["edad"] = 30       # Cambia un valor
persona["pais"] = "España" # Agrega un nuevo par clave-valor
print(persona)