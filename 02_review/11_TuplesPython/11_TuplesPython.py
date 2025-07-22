'''Ahora mismo veremos lo que es una TUPLE, dado que estan se utilizan para
almacenar multiples elementos en una sola variable'''

#Tupla | Es una coleccion que se ordena e inmutable
#Se ordenan | no cambian | permiten valores duplicados
'''Es importante saber quu una tupla sus elementos que contiene dentro de ella
son "indexados "'''

print("Tuples")

this_tuple = ("Juan", 34, "Adorno", True)
#this_tuple.insert("Pedro") | Esto no funciona dado que una tuple, es "inmutable"
print("Elementos de la tuple: ",this_tuple)
print("Cantidad de elementos de la tuple: ",len(this_tuple))


'''Esta es una forma de crear una tuple haciendo uso de la 
misma como si fuera un constructor'''

thattuple = tuple(("manzana", True, 45, "Pedro"))
print(type(thattuple))#Verificamos si es una tuple
print(len(thattuple))#Cantidad de elementos que tiene la tuple