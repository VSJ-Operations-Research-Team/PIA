# -*- coding: utf-8 -*-

import numpy as np


np.set_printoptions(precision=3, suppress=True, linewidth=1000)
probs = np.loadtxt("matrix.csv", delimiter=',')
max_points = len(probs)

init_probs = np.array([0]*max_points)
init_probs[0] = 1


for i in range(1,51):
    ith_step = init_probs@np.linalg.matrix_power(probs, i)
    expected = 0
    for j in range(1,max_points):
        expected += (j+1) * ith_step[j]
    print( f"Step {i}: {expected} " )