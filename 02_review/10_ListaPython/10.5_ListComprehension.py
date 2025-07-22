#Al parecer aqui vamos a entender una sintaxis mucho mas corta cuando deseemos crear una nueva lista
#Basada en valores de una lista existente

fruits = ["manzana", "banana", "cereza", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

print("=" * 40)

personas = ["juan", "gonzalo", "pedro", "rodrigo", "robinson"]
newperson_list = []


for item in personas:
    if "ro" in item:
        newperson_list.append(item)

print(newperson_list)

'''Ahora que estuve probandolo un poco, me doy cuenta que parece ser que funciona como una forma de filtrado y crear una nueva lista
en base lo que se coloque en el "for", quizas me equivoque pero lo veremos más adelante '''

#Pero hay otro modo de hacer un poco mas corto y evitar tanta linea de codigo y es colocar la instruccion de lo que se dfebe de hacer dentro
#de la nueva lista

print("=" * 40)

fruitsi = ["Mango", "Melon", "Pomelo", "Mandarina", "MangoRolo"]
new_fruits = [a for a in fruitsi if "M" in a] #Esta es una forma de hacerlo mucho más corto

print("Esta seria la nueva lista: ", new_fruits)


#Esta seria la sintaxys
# newlist = [expression for item in iterable if condition == True]
