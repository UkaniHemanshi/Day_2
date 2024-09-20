import numpy as np

array_1d = np.array([1,2,3,4])
print("1D array",array_1d)

array_2d = np.array([[1,2],[3,4]])
print("2D array",array_2d)

array_3d = np.array([[1,2],[3,4],[5,6],[7,8]])
print("3D array",array_3d)

ones = np.ones((2,3))
print("array of ones",ones)

step_array = np.arange(0,10,2)
print("array with step size",step_array)

linespace_array = np.linspace(0,1,10)
print("array with linearly spaced value",linespace_array)

random_array = np.random.rand(3,3)
print("array with random values",random_array)


diag_matrix = np.diag([1,2,3,5,6,7,8])
print("diagonal matrix",diag_matrix)

array = np.array([1,2,3])

reshaped_array = array.reshape((2,3))
print("reshaped array",reshaped_array)

empty_1d = np.empty(5)
print("1D empty array",empty_1d)


empty_2d = np.empty((2,3))
print("2D empty array",empty_2d)


empty_3d = np.empty((3,3,2))
print("3D empty array",empty_3d)


empty_int = np.empty((2,2), dtype=int)
print(" empty array",empty_int)

