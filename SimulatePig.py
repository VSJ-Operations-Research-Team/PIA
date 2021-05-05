# -*- coding: utf-8 -*-

import numpy as np
import random

np.set_printoptions(precision=3, suppress=True, linewidth=200)


# Configurar parámetros
throws = 50_000_000
max_points = 100
steps = 50

# Inicializar cuenta
count = [ [ 0 for _ in range(max_points) ] for _ in range(max_points) ]

# Contar trancisiones
points = 0
for _ in range( throws ):
    dice_roll = random.randint(1,6)
    row = max(points-1, 0)
    if dice_roll == 1:
        count[row][0] += 1
    elif points + dice_roll >= max_points:
        count[row][max_points-1] += 1
        count[max_points-1][0] += 1
        points = 0
    else:
        count[row][points + dice_roll-1] += 1
        points = points + dice_roll

# Estimar probabilidades basado en las cuentas
probs = []
for each in count:
    row = []
    for element in each:
        try:
            row.append(element / sum(each))
        except:
            row.append( 0 )
    probs.append(row)

probs = np.asarray( probs )
np.savetxt("matrix.csv", probs, delimiter=',')

