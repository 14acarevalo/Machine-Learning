import numpy as np

# 1. Crear un array con las calificaciones (50 estudiantes x 5 asignaturas)
np.random.seed(42)  # Para reproducibilidad
calificaciones = np.random.uniform(0, 10, size=(50, 5))

# 2. Calcular el promedio de calificaciones por estudiante
promedios_estudiantes = np.mean(calificaciones, axis=1)

# 3. Determinar los estudiantes con un promedio mayor a 7
estudiantes_aprobados = np.where(promedios_estudiantes > 7)[0]  # Índices de los aprobados

# 4. Encontrar la asignatura con el promedio más alto y más bajo
promedio_por_asignatura = np.mean(calificaciones, axis=0)
asignatura_max_promedio = np.argmax(promedio_por_asignatura)
asignatura_min_promedio = np.argmin(promedio_por_asignatura)

# 5. Agregar una nueva columna con los promedios de cada estudiante
calificaciones_con_promedios = np.column_stack((calificaciones, promedios_estudiantes))

# 6. Ordenar los estudiantes por su promedio (de mayor a menor)
indices_ordenados = np.argsort(-promedios_estudiantes)  # Orden descendente
calificaciones_ordenadas = calificaciones_con_promedios[indices_ordenados]

# Mostrar resultados
print("Calificaciones (50 estudiantes x 5 asignaturas):\n", calificaciones)
print("\nPromedios de cada estudiante:\n", promedios_estudiantes)
print("\nEstudiantes aprobados (promedio > 7):", estudiantes_aprobados)
print("\nPromedio por asignatura:", promedio_por_asignatura)
print("Asignatura con el promedio más alto:", asignatura_max_promedio)
print("Asignatura con el promedio más bajo:", asignatura_min_promedio)
print("\nCalificaciones con promedios (última columna):\n", calificaciones_con_promedios)
print("\nCalificaciones ordenadas por promedio (de mayor a menor):\n", calificaciones_ordenadas)
