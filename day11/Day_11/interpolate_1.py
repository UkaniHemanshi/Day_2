from scipy.interpolate import interp1d
import numpy as np

x = np.array([0,1,2,3,4])
y = np.array([0,1,4,9,7])

f=interp1d(x,y,kind='linear')

new_x=2.5
interpolated_value = f(new_x)
print(interpolated_value)