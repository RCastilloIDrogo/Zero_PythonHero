#Ahora mismo vamos a ver algo parecido a lo que uso en PythonString, el uso de arreglos e imprimir una rango establecido
print("---- Slicing String ----")

b = "Hello, Gordon Freeman"
print(b[2:5]) #En este caso, lo que estamos viendo aqui es establecer un rango el cual solo se tomara las letras de ese rango

print("Ahora partiremos desde el rango mas bajo hasta establecer un Limite: ", b[:5])
print("Ahora partiremos inicialmente desde un indice hasta donde finalice: ", b[2:])

#Ademas se puede partir de un indice negativo con la finalidad ya no empezar por la izquiera sino por la derecha
b2 = "Hello, Gorditon Freeman"
print(b2[-5:-2])
