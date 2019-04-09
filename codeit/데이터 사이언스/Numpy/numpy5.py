import numpy as np
array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
array1 > 4
array1 % 2 == 0
booleans = np.array([True, True, False, True, True, False, True, True, True, False, True])
np.where(booleans)
np.where(array1 > 4)
filter = np.where(array1 > 4)
filter
array1[filter]
