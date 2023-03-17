import numpy as nmp

arr1 = nmp.array([1, 2, 3])
mat = nmp.matrix('1 2 3')
print(arr1, mat)

print(nmp.array(arr1, copy=True) is arr1, id(nmp.array(arr1, copy=True)), id(arr1))
print(nmp.array(arr1, copy=False) is arr1, id(nmp.array(arr1, copy=False)), id(arr1))