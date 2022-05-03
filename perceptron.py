# librerias para perceptron
from email import header
from operator import index
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ruta relativa de la database
relative_path = "database.xlsx"
# abrir excel
xls = pd.ExcelFile(relative_path)
# convertir a data frame el excel
df = xls.parse("Sheet1")
# matriz de la databse
matriz = np.array(df)

print(matriz)

# plt.figure(figsize=(7, 7))
# plt.title("¿Tarjeta Platinum?", fontsize=20)
# plt.scatter(matriz[matriz  == 0].T[0],
#             matriz[clases == 0].T[1],
#             marker="x", s=180, color="red",
#             linewidths=5, label="Denegada")
# plt.scatter(matriz[clases == 1].T[0],
#             matriz[clases == 1].T[1],
#             marker="o", s=180, color="blue",
#             linewidths=5, label="Aprobada")
# plt.xlabel("Edad", fontsize=15)
# plt.ylabel("Ahorro", fontsize=15)
# plt.legend(bbox_to_anchor=(1.3, 0.15))
# plt.box(False)
# plt.xlim((0, 1.01))
# plt.ylim((0, 1.01))
# plt.grid()
# plt.show()

# procesamiento de datos


def funcion_activacion_paso(w, x, b):
    z = w * x
    if z.sum() + b > 0:
        return 1
    else:
        return 0
