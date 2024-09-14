from scipy.linalg import inv, det
import numpy as np

matrix = np.array([[4,7],[2,6]])

matrix_inv = inv(matrix)
print(matrix_inv)