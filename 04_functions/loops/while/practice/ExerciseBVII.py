'''Estás programando un sistema para tomar asistencia. El docente ingresa el 
nombre de cada estudiante presente. El ingreso termina cuando se escribe "LISTO".

Al final, el sistema muestra:

Cuántos estudiantes asistieron.
La lista de nombres en orden.'''

class RegistroAsistencia:

    def __init__(self):
        self.asistentes = []

    def tomar_asistencia(self):
        while True:
            nombre = input("Nombre del estudiante (escribe 'LISTO' para terminar): ")

            if nombre.upper() == "LISTO":
                break  # Salir del bucle si se escribe LISTO

            if nombre == "":
                print("El nombre no puede estar vacío.")
                continue  # Saltar esta vuelta si está vacío

            self.asistentes.append(nombre)

        print("\n📋 Lista de asistencia:")
        for idx, estudiante in enumerate(self.asistentes, 1):
            print(f"{idx}. {estudiante}")

        print(f"\n✅ Total de estudiantes presentes: {len(self.asistentes)}")

call = RegistroAsistencia()
call.tomar_asistencia()