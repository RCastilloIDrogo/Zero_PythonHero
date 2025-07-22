#Basicamente lo que se hizo en las listas, podemos hacerlo aqui, teniendo en cuenta que en las tuplas no se pueden cambiar los datos ya ingresados

thattuple = ("Pedro", "Pablo", "Rodrigo")
print("Indice seleccionado positivo: ",thattuple[2])
print("Indice seleccionado negativo: ",thattuple[-2])

#Tambien podemos mostrar el inicio o el final del indice declarando hasta donde queremos que llegue
thattuplee = ("manzana", "banana", "cereza", "naranja", "kiwi", "melón", "mango")
print("Elementos del inicio hasta el indice 4: ", thattuplee[:4])
print("Elementos desde el indice 1 hasta el final ", thattuplee[1:])

#Bueno basicamente podemos hacer esto pero no solo de esta forma sino declarando desde un indice de la tuple
#A otro indice tanto positivo como negativo

print(thattuplee[1:4])
print(thattuplee[-4:-1])

#Podemos determinar cierto elementos en la tupla y preguntar si realmente existe o no
thattuplA = ("manzana", "banana", "cereza", "naranja", "kiwi", "melón", "mango")
if "banana" in thattuplA:
    print(True)
else:
    print(False)