#Declarando Variables de Forma consecutiva - Estableciendo lo que vale por orden
x,y,z = "HalLife", "HalLife2", "HalfLife3"
print("Imprimiendo Variables en Base su Orden: ",(x),(y),(z))

#Declarando que tres variables equivalen a lo mismo
x=y=z = "HalLife"
print("Imprimiendo Variables Equivalentes: ",(x),(y),(z))

#Declaron que una coleccion a variables independientes
Valve = ["HalfLife", "HalfLife2", "HalfLife3"]
x,y,z = Valve
print("Imprimiendo Coleccion: ",x , y ,z)
print("Imprimiendo Coleccion: ",x + y + z) #Este otra forma de separar variables -- TENIENDO QUE EN CUENTA QUE PARA LOS NUMERO ES DIFERENTE


#==============================================================

var1= 14
var2= "Freeman"
var3= 50

print("De esta forma muestra cuando hacemos uso del + en variables de diferente tipo: ", var1 , var2) #Aqui no se usa el más porque son de diferentes tipos
print("De esta forma muestra cuando hacemos uso del + en variables del mismo tipo: ", var1 + var3)