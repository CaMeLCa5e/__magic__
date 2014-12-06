#1.5.14Multithreading.py
"""working through parzen window"""

import numpy as np 

def parzen_estimation(x_samples, point_x, h):
	"""implementation of a hypercube kernal for Parzen-window estimation 

	Keyword args:
		x_sample: training sample, dimensional numpy array
		x: point x for density estimation, 'dx1' - dimensional numpy array
		h: window width

		Returns the predicted pdf as float. 

		"""

	k_n = 0
	for row in x_samples:
		x_1 = (point_x - row[:,np.newaxis])/(h)
		for row in x_i:
			if np.abs(row) > (1/2):
				break
		else: #"completion-else"
			k_n += 1
	return(k_n / len(x_samples)) / (h**point_x.shape[1])


