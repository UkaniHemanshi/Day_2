from scipy.linalg import inv, det
import numpy as np

matrix = np.array([[1,2],[3,4]])

matrix_det= det(matrix)
print(matrix_det)