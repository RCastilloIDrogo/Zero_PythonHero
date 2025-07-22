'''Basicamente lo que vamos hacer aqui es el uso del copiado de una lista, en este caso tener una ya existente podemos
nosotros copiarla'''

this_list = ["Pedro", "Gordon", "Freeman", "Barney"]
lista = this_list.copy()

print("Lista original: ",this_list)
print("Lista copiada: ",lista)

#Pero tambien podemos hacer uso del metodo "list()" para hacerlo en este caso seria de la siguiente forma
print(("=" * 20), "list()",("=" * 20))

my_list = list(this_list)
print(my_list)
