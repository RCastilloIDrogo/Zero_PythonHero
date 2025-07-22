'''Ahora mismo recordando algo importante sobre las tuples, dado que estas son 
inmutable(no pueden agregar o actualizar nuevos elementos)de la misma, pero podemos 
convertir esa tuple en una lista y retornarla a una tuple pero habiendo hecho algunas cambios'''

tuplea = ("Manzana", "Oruga", True, "Paco", "Freeman", 45)
conv = list(tuplea)
conv[3] = "PedroPagon"
tuplea = tuple(conv)

print(tuplea)

'''Considerando que las tuples son inmutables haremos el mismo procedimiento, que en este caso es convertir la tuple
en una lista para usar el metodo append() en ella y luego retornarla a un tuple'''

tthistuple = ("apple", "banana", "cherry")
y = list(tthistuple)
y.append("Jorge")#Agregar un nuevo elemento a la tuple
y.remove("apple")#Eliminar un elemento de la tuple
tthistuple = tuple(y)

print(tthistuple)

#Tambien podemos considerar el uso de una palabra clave para eliminar una tuple por completo "del"
print(("="*20), "Eliminar tuple completa", ("="*20))
tthntuple = ("Jorge", "Abril", "Perico")
del tthntuple
print(tthntuple) #Pero esto marcara un error dado que la tuple no existe