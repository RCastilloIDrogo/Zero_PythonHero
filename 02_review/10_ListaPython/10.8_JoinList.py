#Join List | Unir listas
#Ahora mismo vamos a ver formas las cuales nosotros podemos unir unas lista. Anteriormente ya lo habiamos hecho pero esto es un breve repaso

print(("="*20), "+", ("="*20))

list1 = ["A", "B", "G"]
list2 = [2, 3, 5]

listnew = list1 + list2
print(listnew)

print(("="*20), "append()", ("="*20))
#Otra forma es agregando los item de cada lista uno por uno, eso haciendo uso de append()
list1A = ["A", "B", "G"]
list2A = [2, 3, 5]

for x in list2A:
    list1A.append(x)
print(list1A)

print(("="*20), "extend()", ("="*20))
#Y otra forma de hacerlo es haciendo uso del metodo extend(), el proposito de esta es agregar
#los elementos de una lista a otra
list1B = ["a", "b" , "c"]
list2B = [1, 2, 3]

list1B.extend(list2B)
print(list1B)