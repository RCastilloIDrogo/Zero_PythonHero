'''Un sistema de acceso permite 3 intentos para ingresar la contraseña correcta. 
Si acierta, muestra "Acceso permitido". Si falla 3 veces, muestra "Cuenta bloqueada".

Pistas:
Usa una variable intentos para contar.
Usa while para repetir hasta 3 intentos.
Compara el input con una contraseña predefinida.'''

class ValidacionContraseña():

    def __init__(self):
        self.password = 'python123'        

    def request_password(self):
        i = 0
        max_i = 3
        while i < max_i:
            self.password = input("Por favor, ingrese su contraseña: ")

            if self.password == 'python123':
                print("Acceso permitido")
            else:
                print("Contraseña incorrecta, intentelo de nuevo.")
                i += 1
        
        if i == max_i:
            print("Cuenta bloqueada")

call = ValidacionContraseña()

call.request_password()