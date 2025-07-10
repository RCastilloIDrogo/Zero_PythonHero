#Ahora mismo lo que vamos a ver son los BOOLEANS 

a = 45
b = 35

if a > b:
    print("a es mayor que b")
else:
    print("b es mayo que a")

#Funcion bool() Convierte un valor a su equivalente booleano osea T o F
print("---- Funcion bool() ----")
#Teniendo en cuenta que cuando se hace uso del metodo bool() lo que hace es verificar si tiene contenido es T
#Y sino entonces F

print(bool("Hello"))
print(bool(15))

print("---- Verificando funcion bool ----")
x1 = "Hello"
y1 = 15
z1 = ""
b1 = ()
print(bool(x1))
print(bool(y1))
print(bool(z1))
print(bool(b1))


#Booleano en una Clase
print("---- BoolClass ----")
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


#Basicamente ahora estamos declarando que nuestra funcion retorne a True y cuando lo haga va imprimir YES!
#Y en el caso que no, seria FALSE!

print("---- Retornando Valor bool ----")
def myFunction() :
  return False

if myFunction():
  print("YES!")
else:
  print("NO!")


print("---- Isintance ----")
#Comprueba si una variable o valor es de un cierto tipo de datos.
x = 200
print(isinstance(x, float))
print(isinstance(x, str))
print(isinstance(x, int))
print(isinstance(x, complex))
#Basicamente esta es una forma de decir que esta confirmando que la variable es de cierto tipo
