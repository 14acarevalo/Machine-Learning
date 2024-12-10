import numpy as np

# 1. Crear un array de gastos (5 personas x 12 meses)
np.random.seed(42)  # Para reproducibilidad
gastos = np.random.uniform(100, 2000, size=(5, 12))

# 2. Calcular el gasto total anual de cada persona
gasto_anual = np.sum(gastos, axis=1)

# 3. Determinar el mes con el mayor gasto para cada persona
mes_mayor_gasto_persona = np.argmax(gastos, axis=1)

# 4. Encontrar el mes con el mayor promedio de gastos considerando a todas las personas
promedio_mensual = np.mean(gastos, axis=0)
mes_mayor_promedio = np.argmax(promedio_mensual)

# 5. Identificar a la persona que gastó más en total en el año
persona_mas_gastadora = np.argmax(gasto_anual)

# 6. Añadir una fila con los gastos promedio mensuales
gasto_promedio_por_mes = np.mean(gastos, axis=0)
gastos_actualizado = np.vstack([gastos, gasto_promedio_por_mes])

# 7. Guardar el array actualizado en un archivo .npy y cargarlo nuevamente
np.save('gastos_actualizado.npy', gastos_actualizado)
gastos_cargado = np.load('gastos_actualizado.npy')

# Mostrar resultados
print("Gastos mensuales (5 personas x 12 meses):\n", gastos)
print("\nGasto total anual de cada persona:\n", gasto_anual)
print("\nMes con el mayor gasto por persona (índices):\n", mes_mayor_gasto_persona)
print("\nMes con el mayor promedio de gastos (índice):", mes_mayor_promedio)
print("\nPersona que gastó más en total (índice):", persona_mas_gastadora)
print("\nGastos actualizados (con promedio mensual añadido):\n", gastos_cargado)
