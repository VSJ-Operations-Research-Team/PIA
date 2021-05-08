# -*- coding: utf-8 -*-

import numpy as np


probs = np.loadtxt("matrix.csv", delimiter=',')
max_points = len(probs)

init_probs = np.array([0]*max_points)
init_probs[0] = 1

expectancies = []
for row in probs:
    expectancy = 0
    # Empezamos desde la segunda col, porque la primera da 0 y es más fácil
    # de manejar de esta forma
    for i in range(1, max_points): 
        expectancy += (i+1) * row[i]
    expectancies.append(expectancy)


min_diff_exp = abs( expectancies[0] )
min_diff_state=0

# No consideramos 100 puntos porque la esperanza es 100 y porque es el objetivo
for i in range(1, max_points-1):    
    if abs( expectancies[i] - (i+1) ) < min_diff_exp:
        min_diff_exp = abs( expectancies[i] - (i+1) ) 
        min_diff_state = i+1

print(f'''The minimum amount of difference between
the state and the expectancy is {min_diff_exp}
on the state {min_diff_state}. The calculated expectancý was:
    {expectancies[min_diff_state-1]}''' )
