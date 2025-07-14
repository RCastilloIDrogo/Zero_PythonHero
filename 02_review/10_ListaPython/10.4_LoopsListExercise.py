#Python loops es una forma de decir que recorre elementos haciendo uso de un "for" en bucle

print("---- Loop - Python ----")
list = ["Pepe", "Dedo", "Papotico"]

for item in list:
    print(item)


print("============================")
#Haciendo uso de estos loops podemos recorrer los números de índice, osea puede recorrer esta lista
#Refiriendose a su numero de indice

listt = ["pepino", "palanca", "manolorojas"]

for item in range(len(listt)):
    print(listt[item])


print("============================")
#Ahora mismo debemos hacer uso del While, ademas haremos uso de la funcion len() para  determinar la
#Longitud de la isla 

print("---- While - Lopp ----")

thislist = ["apple", "python", "MySql"]
item1 = 0
while item1 < len(thislist):
    print(thislist[item])
    item1 +=1