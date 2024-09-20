import numpy as np

random_2D_array = np.random.randint(10, 100, size=(5, 3))
transpose_2Darray = random_2D_array.T

mean_original = np.mean(random_2D_array)
print(mean_original)

mean_transpose = np.mean(transpose_2Darray)
print(mean_transpose)

print(random_2D_array)
print(transpose_2Darray)