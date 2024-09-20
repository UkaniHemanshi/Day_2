import numpy as np

list1 = [2,3,41,4,5]
list2 = [1,2,3,4,5]
list3 = [3,4,5,6,7]
list4 = [5,6,7,8,9]

arr1 = np.array([list1,list2])
arr2 = np.array([list3,list4])

# print(f"Memberwise addition:{np.add(arr1[0],arr1[1])}")

print(np.add(arr1,arr2))
print(np.subtract(arr1,arr2))
print(np.multiply(arr1,arr2))
print(np.exp(arr1))
