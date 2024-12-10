import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

X = 4*3*np.random.rand(100,1)
y = 4+3*X+np.random.rand(100,1)
z = y/X


print("La longitud de la gráfica es igual a: ", len(X));

plt.plot(X,y, "b.")
plt.xlabel("Equipos afectados")
plt.ylabel("Coste incidencias")
plt.show()

data = {"Equipos afectados": X.flatten(),
        "Coste incidencias": y.flatten(),
        "Coste medio incidencias": z.flatten()}

df = pd.DataFrame(data)
CosteIncidente = df["Coste incidencias"]
CosteMayor = df["Coste medio incidencias"]
EquiposMasAfectados = df["Equipos afectados"]

print(CosteIncidente.tail(10))
print(CosteMayor.head(5))
print(EquiposMasAfectados.head(5))
