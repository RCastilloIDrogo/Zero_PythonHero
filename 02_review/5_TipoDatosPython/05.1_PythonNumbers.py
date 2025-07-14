#Numero en python se diferencia de tres formas
#Integer: Estos pueden ser numero positivos, negativos sin decimales
#Float: Estos pueden ser numero positivos, negativos con decimales
#Complex: Estos numero al final se escriben con una "j" de forma imaginaria
c = 1 #int
c1 = -1

v = 2.4 #float
v = -2.4
b = 1j #complex
b1 = -1j

print(type(c))
print(type(v))
print(type(b))

#En python con respecto a los numero hay tipos de conversion en base a lo que se es
print("-----Type Conversion-----")

x = 1
y = 2.6
z = -1j

#Convertir de Int a float
a = float(x)

#Convertir float a Int

b = int(y)

#Convertir de Int a Complex

c = complex(z)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))