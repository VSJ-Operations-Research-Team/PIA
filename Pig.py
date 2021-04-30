# -*- coding: utf-8 -*-

import numpy as np
import random

np.set_printoptions(precision=3, suppress=True, linewidth=200)

# Configurar parámetros
throws = 5_000_000
max_points = 100
steps = 50

# Inicializar cuenta
count = [ [ 0 for _ in range(max_points-1) ] for _ in range(max_points-1) ]

# Contar trancisiones
points = 0
for _ in range( throws ):
    dice_roll = random.randint(1,6)
    row = max(points-1, 0)
    if dice_roll == 1:
        count[row][0] += 1
    elif points + dice_roll >= max_points:
        points = 0
    else:
        count[row][points + dice_roll-1] += 1
        points = points + dice_roll

# Estimar probabilidades
probs = []
for each in count:
    row = []
    for element in each:
        try:
            row.append(element / sum(each))
        except:
            row.append( 0 )
    probs.append(row)
probs = np.array( probs )

# Solo puedes empezar con 0 puntos
initial_probs = np.array([ 0 for _ in range(max_points-1) ])
initial_probs[0] = 1

# Buscar cantidad de lanzamientos que maximizen las
# probabilidades de llegar a 100 puntos
max_prob = -1
max_prob_pos = 0
result = probs
for i in range(steps):
    result = result @ probs
    if (initial_probs@result)[-1] > max_prob:
        max_prob = (initial_probs@result)[-1]
        max_prob_pos = i+2
    
print(max_prob_pos, ".-", max_prob)