'''Pide calificaciones del 1 al 5 de varios clientes.
Cuando el usuario escribe 0, termina la encuesta.
Al final, muestra el promedio de calificaciones.'''

class CalificacionesEscolares():

    def __init__(self):
        self.alumnos = {}

    def ingresa_datos(self):
        try:
            total_alumnos = int(input("Cuantos alumnos deseas ingresar? "))
        except ValueError:
            print("Por favor, ingresa un numero valido")
            return
        
        contador = 0
        while contador < total_alumnos:
            nombre = input(f"Ingrese el nombre del alumno #{contador + 1}: ")
            self.alumnos[nombre] = []

            print(f"Ingrese las calificaciones para {nombre} (Escribe 0 para terminar)")
            while True:
                try:
                    nota = float(input("Calificacion (1 a 5): "))
                    if nota == 0:
                        break
                    if 1<= nota <=5:
                        self.alumnos[nombre].append(nota)
                    else:
                        print("La calificacion debe estar entre 1 y 5")
                except ValueError:
                    print("Por favor, ingresa un numero valido.")
            contador += 1

    def mostrar_promedios(self):
        print("\nPromedios por alumno:")
        suma_total = 0
        cantidad_notas = 0

        alumnos_lista = list(self.alumnos.items())
        indice = 0

        while indice < len(alumnos_lista):
            nombre, notas = alumnos_lista[indice]
            if notas:
                promedio = sum(notas) / len(notas)
                print(f"{nombre}: {promedio:.2f}")
                suma_total += sum(notas)
                cantidad_notas += len(notas)
            else:
                print(f"{nombre}: Sin calificaciones")
            indice += 1

        if cantidad_notas > 0:
            promedio_general = suma_total / cantidad_notas
            print(f"\nPromedio general de todas las calificaciones: {promedio_general:.2f}")
        else:
            print("\nNo se ingresaron calificaciones.")

# Uso del programa
calificaciones = CalificacionesEscolares()
calificaciones.ingresa_datos()
calificaciones.mostrar_promedios()