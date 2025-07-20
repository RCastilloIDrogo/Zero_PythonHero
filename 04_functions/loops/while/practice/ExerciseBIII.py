'''Imagina que estás creando el sistema de caja de una tienda.
El programa debe pedir el precio de cada producto (uno por uno) al usuario.
El usuario escribe "0" cuando ya no tiene más productos.
El programa debe mostrar el total a pagar.'''

class CajaTienda:
    def __init__(self):
        self.total = 0

    def iniciar(self):
        precio = 1  # cualquier valor distinto de 0 para entrar al while
        while precio != 0:
            precio = float(input("Ingresa el precio del producto (0 para terminar): "))
            if precio != 0:
                self.total += precio

        print("🧾 Total a pagar:", self.total)


call = CajaTienda()

call.iniciar()