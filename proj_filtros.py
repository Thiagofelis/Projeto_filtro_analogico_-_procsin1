import numpy as np

def projeto_pb (h_0, h_1, c_2, alpha):
	a = h_0 / (c_2 * h_1)
	b = 1/(h_1 * alpha * (c_2 ** 2))
	r_1 = (a + np.sqrt(a ** 2 - 4 * b)) / 2
	r_2 = (a - np.sqrt(a ** 2 - 4 * b)) / 2
	c_1 = c_2 * alpha
	return [r_1, r_2, c_1, c_2]

def projeto_pa (h_0, h_1, r_1, alpha):
	a = h_0 / (r_1 * h_1)
	b = 1/(h_1 * alpha * (r_1 ** 2))
	c_1 = (a + np.sqrt(a ** 2 - 4 * b)) / 2
	c_2 = (a - np.sqrt(a ** 2 - 4 * b)) / 2
	r_2 = r_1 * alpha
	return [r_1, r_2, c_1, c_2]
	
def alpha_min (h_0, h_1):
	return 4 * h_1 / (h_0 ** 2)



	
