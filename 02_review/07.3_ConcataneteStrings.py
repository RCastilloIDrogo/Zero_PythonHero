#Basicamente esta es una de las formas de concatenar en strings
#Anteriormente ya lo hemos visto haciendo uso del "+"

a = "Hello"
b = "Gordon"

print("Concatenacion: ",a + b)

#Formato de los mismos STR
#Hay que tener en cuenta que cuando hablamos de STR con float, etc no podemos concatenarlos 
# con el uso del "+" o "," sino haciendo uso de los "{}"

print("----- Formato de los Strings -----")
age = 56
a = f"My name is Gordon,I am {age} "
print(a)

#Ahora nosotros tambien podemos decir que el numero puede que sea entero
# Pero al momento de imprimirlo podemos hacer uso de dos decimales a pesar que es entero de la siguiente forma
print("---- Convertir una Variable entera a una Decimal ----")
price = 56
txt = f"The price is {price:.2f} dollars"
print(txt)

#Ademas de eso podemos multiplicar, sumar, restar o dividir dentro de un mismo STR
print("---- Multiplicar dentro de un String ----")
txt = f"The price is {90 * 800} dollars"
print(txt)