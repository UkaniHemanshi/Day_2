import numpy as np
random_2D_array = np.random.randint(50, 100, size=(5, 5))
print(random_2D_array)

random_2D_array[1:4,1:4] = np.zeros((3,3))
print(random_2D_array)



