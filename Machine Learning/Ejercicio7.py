import numpy as np

# 1. Crear un array de ventas aleatorias (30 días, 5 productos)
ventas = np.random.randint(0, 101, size=(30, 5))

# 2. Encontrar los días con mayores ventas para cada producto (por columna)
dias_mayores_ventas = np.argmax(ventas, axis=0)  # El índice del día con mayor venta para cada producto

# 3. Calcular el promedio de ventas por producto (por columna)
promedio_ventas = np.mean(ventas, axis=0)

# 4. Encontrar el producto que más se vendió durante el mes (sumando las ventas de cada producto)
total_ventas_por_producto = np.sum(ventas, axis=0)
producto_mas_vendido = np.argmax(total_ventas_por_producto)

# 5. Encontrar el día con mayores ventas globales (sumando todas las ventas en un día)
ventas_diarias_totales = np.sum(ventas, axis=1)
dia_mayores_ventas_globales = np.argmax(ventas_diarias_totales)

# Mostrar resultados
print("Ventas de la tienda durante 30 días para 5 productos:\n", ventas)
print("\nDías con mayores ventas por producto:", dias_mayores_ventas)
print("\nPromedio de ventas por producto:", promedio_ventas)
print("\nProducto más vendido (índice):", producto_mas_vendido)
print("\nDía con mayores ventas globales (índice):", dia_mayores_ventas_globales)
