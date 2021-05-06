import numpy as np
import pandas as pd

probs = np.loadtxt("matrix.csv", delimiter=',')
max_points = 100

indice = []
for i in range(max_points + 1):
    if(i==1):
        continue
    indice.append(i)

power = np.linalg.matrix_power(probs, 10)
power = np.asarray( power )
np.savetxt("matrix_power_10.csv", power, delimiter=',')

for i in range(max_points):
    for j in range(max_points):
        probs[i][j] = probs[i][j]*100

df = pd.DataFrame(probs, index = indice, columns = indice)
df.to_excel('Matriz_Transicion.xlsx', sheet_name='Hoja1')