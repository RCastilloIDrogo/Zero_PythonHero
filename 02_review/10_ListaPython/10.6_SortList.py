#Ahora veremos la listas de clasificacion, basicamente se hara uso por el momento el metodo "sort()"
#El metodo sort() | ordena la lista de forma alfanumericamente ascendente

this_list = ["naranja","banana", "pepinillo", "arroz", "camote"]
this_list.sort()

print(this_list)

#Teniendo en cuenta que esto lo hace de forma ascendente, pero se puede hacerlo de forma inversa?. 
#En este caso de forma descendente. Basicamente es lo mismo pero se hace un breve agregado dentro del metodo sort()

print("=" * 40)


this_listi = ["naranja","banana", "pepinillo", "arroz", "camote"]
this_listi.sort(reverse=True)

print(this_listi)

#Ademas esto se puede hacer uso pero con una funcion "def"

def myfunc(n):
    return abs(n)



thislistA = [100, 40, 560, 590, 23, 400, 330]
thislistA.sort(key = myfunc)


print("Llamando a la funcion: ",thislistA)

#Acabo de darme cuenta que si yo coloco el numero mas alto que tengo, en este caso lo hara de forma descencdiente y
#Me mostrara lo siguiente "Llamando a la funcion:  [590, 560, 400, 330, 100, 40, 23]"

#Pero en el caso que yo colo que el numero bajo, no el mas bajo me sale lo siguiente "Llamando a la funcion:  [40, 23, 100, 330, 400, 560, 590]"
#Y si al retornar le quito el numero a seleccionar, me da como resultado esto de aqui: ""

'''Detalle importante dado que estuve probando, si hacemos lo mismo pero para un "str" no va funcionar por obvias razones
dado que no se puede restar un str'''

#def strfunc(x):
    #return abs(x - "Mario")

#thislistB = ["Pedro", "Mario", "ADOLFO", "HITLER"]
#thislistB.sort(key = strfunc(str.lower))
#print("Llamando a la funcion str: ", thislistB)

#Por ello se hace la siguiente forma que veremos a continuacion

thislistJ = ["banana", "Orange", "Kiwi", "cherry"]
thislistJ.sort(key = str.lower)
print(thislistJ)


#Ademas podemos hacer que el orden de esto sea el reverso del mismo haciendo uso de "reverse()"
print(("=" * 20), "reverse()",("=" * 20))

lista = ["banana", "orange", "kiwi", "cherry"]
lista.reverse()

print("Este el reverso de la lista",lista)
