# Exercise: NumPy Basics

import numpy as np
arr=np.arange(9)
print(arr)
arr2=arr.reshape(3,3)
print(arr2)
arr3=arr*2
print(arr3)
mean=np.mean(arr)
median=np.median(arr)
mode=np.std(arr)
print("mean is ",mean," median is ",median," std is ",mode)
arr4=np.arange(10,19)
print(arr4)
arr5=arr2.T
print(arr5)
arr6=arr*arr
print("arr is ",arr6)
arr7=np.dot(arr,arr5)
print(arr7)

# Exercise: Slicing NumPy Arrays
import numpy as np
arr=np.arange(20)
print(arr)
arrE=arr[5:11]
print(arrE)
arrO=arr[::2]
print(arrO)
arr_2d=np.arange(16).reshape(4,4)
print(arr_2d)
arr_2d_col_2=arr_2d[:,1]
print(arr_2d_col_2)
arr_2d_row_3=arr_2d[2,:]
print(arr_2d_row_3)
arr_2d_2x2_TR=arr_2d[:2,:2]
print(arr_2d_2x2_TR)
arr_2d_2x2_BR=arr_2d[2:,2:]
print(arr_2d_2x2_BR)
arr_2d_reverse=arr_2d[::-1,::-1]
print(arr_2d_reverse)