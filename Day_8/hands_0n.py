import numpy as np

array_1d = np.array([1,2,3,4])
print("1D array\n",array_1d)

array_2d = np.array([[1,2],[3,4]])
print("2D array\n",array_2d)

array_3d = np.array([[1,2],[3,4],[5,6],[7,8]])
print("3D array\n",array_3d)

def describe_array(*args):
        for i in args:
            print(f"array dimension is:{i.ndim}")
            print(f"array size is : {i.size}")
            print(f"array shape is: {i.shape}")
            print(f"array datatype is: {i.dtype}\n")
describe_array(array_1d,array_2d,array_3d)