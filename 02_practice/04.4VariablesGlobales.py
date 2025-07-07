#Se creo una variable fuera de la misma funcion para hacer llamado de la misma dentro de ella
gordon = "Freeman"

def blackmesa():
    print("Doctor" + gordon)
blackmesa()

#Pero esto es totalmente diferente si en el caso que hay una variable fuera de la funcion y dentro de esa misma funcion son la mimsa
#La variable dentro de la funcion se tomar de manera local

barney = "blueShift"

def City17():
    barney = "Police"
    print("---Dentro de la función---")
    print("Barney is a: " + barney)
City17()

print("Fuera de la funcion: " + barney)

#Peroo tambien podemos hacer que esa variable que esta dentro de la funcion sea GLOBAL

barney = "blueShift"

def City17():
    global barney
    barney = "Police"
    print("---Dentro de la función (Variable Global)---")
    print("Barney is a: " + barney)
City17()

print("Fuera de la funcion: " + barney)