#Ahora mismo lo que vamos aprender es basicamente en eliminar un item dentro de una lista

#
thislistT = ["Perico", "Mike", "Rogelio", 50, True, False]
thislistT.remove("Perico")

#Vamos a probar si se puede borrar mediante el indice del item
#thislistT.remove([0]), esto no funciona de esa forma por ello vamos hacer uso de "pop()"

thislistT.pop(3) #En este caso elimina el true, dado que anteriormente se elimino "Perico"
#Y el orden del indice se actualiza
print(thislistT)

thislistTA = ["Pablo", "Meruem", "Roger", 20, True, False]
#Pero en el caso que no definimos un "index" se eliminara el item siguiente
print("Pop sin index: ",thislistTA.pop())
print("Lista actualizada:", thislistTA)



#TAMBIEN PODEMOS ELIMINAR UN ITEM DE LA SIGUIENTE MANERA
print("---- KEYWORD - del -----")
thislistII = ["apple", "banana", "cherry"]
del thislistII[0]# tambien podemos eliminar toda la lista de la siguiente forma "del thislistII"
print(thislistII)

print("---- METHOD - clear -----")
thislistA = ["Gordon", "Pepinillo", "cherry"]
thislistA.clear()
print("Limpiando la lista creada: ",thislistA)