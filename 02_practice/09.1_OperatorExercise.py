def operar(valor_inicial, operador, operando):
    if operador == '+=':
        valor_inicial += operando
    elif operador == '-=':
        valor_inicial -= operando
    elif operador == '*=':
        valor_inicial *= operando
    elif operador == '/=':
        valor_inicial /= operando
        
    elif operador == '!=':
        return valor_inicial != operando
    elif operador == '==':
        return valor_inicial == operando
    elif operador == '>':
        return valor_inicial > operando
    elif operador == '**':
        return valor_inicial ** operando
    else:
        raise ValueError("Operador no soportado.")
    
    return valor_inicial


# Ingreso de datos por el usuario
v1 = input("Ingrese la primera variable: ")
v2 = input("Ingrese la segunda variable: ")
operador = input("Ingrese el operador (+=, -=, *=, /=, !=, ==, >, **): ")

# Convertir las variables a números (puedes usar float si quieres permitir decimales)
v1 = int(v1)
v2 = int(v2)

# Aplicar operación
resultado = operar(v1, operador, v2)

# Mostrar resultado
print("Resultado:", resultado)
