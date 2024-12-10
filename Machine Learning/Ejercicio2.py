import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


##Añadir una columna calculada

X = 4*3 *np.random.rand(100,1)
y = 4+3*X+ np.random.randn(100,1)
z= y/X

print("La longitud es igual a: ", len(X))

plt.plot(X, y, "b.")
plt.xlabel("Equipos afectados")
plt.ylabel("coste_incidentes")
plt.show()

data = {"Equipos afectados": X.flatten(), 
        "coste_incidentes": y.flatten(),
        "Costo medio por equipo": z.flatten()}

print(data)