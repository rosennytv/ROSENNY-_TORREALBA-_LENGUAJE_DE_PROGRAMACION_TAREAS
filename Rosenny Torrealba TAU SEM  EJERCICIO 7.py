import random

# 1. Definimos una lista de estudiantes con nombres aleatorios
lista_estudiantes = ["Carlos Mendoza", "Ana Gabriel", "Luis Fernando", "María Elena", "Jorge Luis"]

# 2. Creamos el diccionario vacío para almacenar las calificaciones
registro_calificaciones = {}

# 3. Asignamos una calificación aleatoria a cada estudiante
for estudiante in lista_estudiantes:
    # Generamos una nota flotante aleatoria entre 7.0 y 10.0 y la redondeamos a 1 decimal
    nota_aleatoria = round(random.uniform(7.0, 10.0), 1)

    # Asignamos la nota al estudiante en el diccionario
    registro_calificaciones[estudiante] = nota_aleatoria

# 4. Mostramos el resultado final recorriendo el diccionario
print("--- REGISTRO DE CALIFICACIONES ---")
for estudiante, calificacion in registro_calificaciones.items():
    print(f"Estudiante: {estudiante} | Calificación: {calificacion}")