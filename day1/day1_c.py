import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

ele_mul = A*B
print("逐元素相乘 A*B:\n",ele_mul)

mat_mul = A@B
print("矩阵点乘 A@B:\n",mat_mul)