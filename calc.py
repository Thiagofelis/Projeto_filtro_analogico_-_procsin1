from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import control

import csv

# p = a +- ib

# polos passa-baixa
a_l = [-874966.806199, -2106952.38405]
b_l = [6178838.45562, 2565953.73316]

# polos passa-alta
a_h = [-7545.71146673, -886.982577377]
b_h = [9189.55105676, 6263.69139919]

k = 3.81332746617e+26

# H[i][1] / (s^2 + H[i][0] * s + H[i][1]) 
H_l = [ [-2 * a_l[0], a_l[0] ** 2 + b_l[0] ** 2] ,
	    [-2 * a_l[1], a_l[1] ** 2 + b_l[1] ** 2] ]

# s^2 / (s^2 + H[i][0] * s + H[i][1]) 
H_h = [ [-2 * a_h[0], a_h[0] ** 2 + b_h[0] ** 2] ,
	    [-2 * a_h[1], a_h[1] ** 2 + b_h[1] ** 2] ]


K = k / (H_l[0][1] * H_l[1][1])

print(H_l)
print(H_h)
print(K)



