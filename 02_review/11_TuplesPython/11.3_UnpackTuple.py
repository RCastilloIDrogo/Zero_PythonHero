'''Cuando creamos una tupla , al asignar un valor se le llama "empaquetar" '''
frutas = ("carro", "pedro", "jose", "papotico")
print(frutas)

#Pero tambien se puede hacer un termino llamado "Desempaca" que nos permite extraer 
#los valores en variables

frutast = ("manzana", "toronga", "pedro")
(verde, rojo, marron) = frutast

print(verde)
print(rojo)
print(marron)

#El uso del "*" en las tuples por lo que entiendo, es en enlazar lo que se va empaquetar por variable y el sobrante que tenga el "*"
#Se le asigna los demas elementos pero como una lista

print(("="*20), "Uso del '*'", ("="*20))

frutase = ("manzana", "banana", "cereza", "fresa", "frambuesa")

(verde, amarillo, *rojo) = frutase

print(verde)
print(amarillo)
print(rojo)

