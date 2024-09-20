import numpy as np

array = np.arange(0,17,1)

square_root = np.sqrt(array)
print(square_root)1

combined  = np.vstack((array,square_root))

np.savetxt('square_root_results.csv', combined,delimiter=',')

print(combined)