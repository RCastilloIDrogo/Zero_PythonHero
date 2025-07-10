#Basicamente en este pequeño ejercicio podemos ver como agregar un nuevo item a la lista, ademas de su posicion
#Usabamos append para agregar un nuevo item, pero no en que indice

#thislist.append(4, "Pepingo")  PERO ESTO NO ESTA BIEN!!!!
print("---- Insert - Listas ----")
thislist = ["apple", "banana", "cherry"]
#Basicamente en la linea de abajo estamos dando referencia del indice, más el item por insertar
thislist.insert(2, "watermelon")
print(thislist)

print("---- Extend - Listas -----")
#thislist = ["apple", "banana", "cherry"], lo comentamos porque lo tenemos arriba
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)#Lo que hacemos es lo siguiente
#El contenido de tropical se va trasladar a la otra lista creada
print("Version extendida: ",thislist)

#Dato Importante: No solo esto funciona con listas, sino tambien haciendo uso 
#De tuples, sets y diccionarios en python

thistuple = ("kiwi", "MangoAngo")

thisdictionary= {
    "Nombre" : "Pedro",
    "Apellido" : "Rogelio",
    "Edad" : 67
}

print("---- Tuples ----")

thislist1 = ["Suegra", "Palanca", "RedStone"]
thislist1.extend(thistuple)
print("Version con Tuples: ",thislist1)

print("---- Dictionary ----")

thislist2 = ["Perico", "Ardilla", "Papas"]
thislist2.extend(thisdictionary)
print("Version con Tuples: ",thislist2)
