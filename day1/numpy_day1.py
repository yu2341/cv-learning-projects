import numpy as np
arr1 =  np.array([1,2,3,4,5])
print("一堆数组 arr1:",arr1)
print("arr1 形状：",arr1.shape)

arr2 = np.array([[1,2,3],[4,5,6]])
print("arr2:",arr2)
print("arr2 形状：",arr2.shape)

zero_mat = np.zeros((3,3))
one_mat = np.ones((2,2))
print("3*3全0矩阵：\n",zero_mat)
print("2*2全1矩阵\n",one_mat)

arr3 = np.arange(0,10,2)
print("arange数组:",arr3)


