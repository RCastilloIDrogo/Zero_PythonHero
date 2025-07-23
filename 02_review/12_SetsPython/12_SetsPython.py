''' Set | Es una estructura de datos usada para almacenar elementos, y es similar a una lista.
Pero con ciertas diferencias:
No pueden haber elementos duplicados | Son desordenados | Son inmutables | Pero se puede agregar o elimnar elementos '''

thisset = {"apple", "manzana", "pedrito"}
print(thisset)

#Hay otra forma para crear un set haciendo el uso de lo siguiente "set()"

s = set([4, 4, 4, 5, 6, 7, 8]) #En este caso estariamos haciendo uso de un constructor
print(s)
print(type(s))

#Como habiamos visto, no puede haber elementos duplicados, en este caso el resultado
#Del mismo set al imprimirlo es el siguiente: {4, 5, 6, 7, 8}

#Ademas algo a considerar en los set, el valor de 1 con True se consideran iguales
#Al igual que False con 0
'''En este caso si tenemos un set con esos valores por asi decirlo duplicados, 
se eliminaran en este caso en "0" y el "1" '''

print(("="*20),"True and False | set",("="*20))
setthis = {12, 14 , True, False, 0, 1, "Manzana", "Perro", "Gordon Freeman"}
print("Este es el set sin elementos duplicados:", setthis)

#En este caso el resultado que nos da al imprimir este set es el siguiente
#{False, True, 'Perro', 'Manzana', 'Gordon Freeman', 12, 14}