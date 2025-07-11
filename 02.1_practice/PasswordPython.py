import random
import string

longitud = int(input("Cuantos caracteres quieres que tenga tu contraseña? "))

caracteres = string.ascii_letters + string.digits + string.punctuation

contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))

print(f"Tu contraseña generada es: {contraseña}")