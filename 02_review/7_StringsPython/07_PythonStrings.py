#Cuando hablamos de Strings podemos mostrarlos al imprimirlos haciendo uso de "" o ''
print("Half Life más cerca que nunca")
print('Half Life más cerca que nunca')

#Basicamente podemos hacer uso de estas comillas dentro de las otro tipo de comillas para mostrarlas
print('--- Quotes Inside Quotes ---')
print('Half Life más "cerca que nunca"')
print("Half Life más 'cerca que nunca'")

#Tambien podemos hacer uso de una variable que contenga un str para imprimirlo

a = 'Gordon Freeman'
print(a)
#Ademas podemos ver el tipo de esta variable
print(type(a))

print("---- MultiLines Strings -----")
#Al parecer esto se hace haciendo uso de 3x de comillas dobles y separando estas lineas con comas
a1 = """ Gordon Freeman más cerca que nunca,
Tiki tiki tiki tiki tiki,
Tengo hambre we, embeces"""

#Y como hicimos al inicio tambien se puede hacer uso de estas comillas simples
a1 = '''Gordon Freeman más cerca que nunca,
Tiki tiki tiki tiki tiki,
Tengo hambre we, embeces'''

print(a1)

print('---- Strings are Arrays ----')
#Basicamente podemos hacer uso de un array e imprimir como tal el "indice" o valor de lugar de la variable impresa
#Ademas podemos establecer un rango para mostrar las letras o en este caso una palabra
a = "Hello, Gordon Freeman"
print(a[0:5])

print("---- Looping Through a String ----") #Recorrer una cadena
for x in "banana": #Basicamente esto hace un recorrido de las letras de la palabra "banana"
    print(x)

print("---- String Length ----")# len() la función devuelve la longitud de una cadena
gf = "Hola, Gman"
print(len(gf))

print("---- Check String ----")#Aqui podemos verificar si la palabra seleccionada esta dentro de la variable
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' ins present.")

#Ademas esto tambien podemos hacer uso de lo contrario, para verificar si cierta palabra no esta dentro de la Variable(Cadena)
txt = "The best things in life are free!"
print("Gman" not in txt)

txt = "The best things in life are free!"
if "Gman"   not in txt:
    print("No, 'Gman' is NOT present.")