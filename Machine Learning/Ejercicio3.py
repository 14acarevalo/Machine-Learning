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

data = {"Equipos afectos": X.flatten(),
        "Coste incidencias": y.flatten(),
        "Coste medio incidencias": z.flatten()}

df = pd.DataFrame(data)

CosteMayor = df[df["Coste incidencias"] > 30]
print(CosteMayor)

