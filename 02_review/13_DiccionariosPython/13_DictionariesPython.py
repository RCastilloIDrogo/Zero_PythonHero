''' 
Dict | Es una estructura de datos usada para almacenar datos en pares clave:valor, 
y es diferente a listas o sets por lo siguiente:

- No pueden haber claves duplicadas
- Los valores sí pueden repetirse
- Son ordenados (desde Python 3.7)
- Son mutables (se pueden agregar, eliminar y modificar elementos)
'''

thisdict = {"nombre": "Ana", "edad": 30, "ciudad": "Lima"}
print(thisdict)

# También se puede crear un diccionario usando el constructor dict()
d = dict(nombre="Carlos", edad=25, ciudad="Bogotá")  # En este caso se usa el constructor
print(d)
print(type(d))

# Si se repiten las claves, la última sobrescribe a la anterior
repetido = {
    "nombre": "Luis",
    "nombre": "Pedro"  # Este sobrescribe al anterior
}
print(repetido)
# Resultado: {'nombre': 'Pedro'}

# Algo curioso: True y 1 se consideran claves iguales, al igual que False y 0
''' 
Si usas True y 1 como claves, se sobrescriben.
Lo mismo con False y 0.
'''

print(("="*20), "True and False | dict", ("="*20))
dictthis = {
    True: "valor1",
    1: "valor2",
    False: "valor3",
    0: "valor4",
    "nombre": "Pedro",
    "ciudad": "Arequipa"
}
print("Este es el diccionario sin claves duplicadas:", dictthis)
# Resultado esperado:
# {True: 'valor2', False: 'valor4', 'nombre': 'Pedro', 'ciudad': 'Arequipa'}

# Métodos útiles
print("="*20, "Métodos útiles", "="*20)
print("Claves:", dictthis.keys())
print("Valores:", dictthis.values())
print("Pares clave:valor:", dictthis.items())

# Podemos agregar, modificar y eliminar elementos
dictthis["edad"] = 40             # Agregar
dictthis["nombre"] = "Lucía"      # Modificar
del dictthis[False]               # Eliminar usando clave
print("Diccionario actualizado:", dictthis)
