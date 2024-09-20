import numpy as np

matrix1 = np.random.randint(1, 11, size=(4, 2))
matrix2 = np.random.randint(1, 11, size=(2, 3))

multi_matrix = np.matmul(matrix1,matrix2)

transpose_multi_matrix = multi_matrix.T
print(matrix1)
print()
print(matrix2)
print()
print(multi_matrix)
print()
print(transpose_multi_matrix)
