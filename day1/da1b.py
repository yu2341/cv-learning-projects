import numpy as np

mat = np.array([[10,20,30,40],
                [50,60,70,80],
                [90,100,110,120]])

print("原矩阵；\n",mat)

row0 = mat[0,:]
print("第0行：",row0)

col1 = mat[:,1]
print("第1列：",col1)

sub_mat = mat[0:2,0:3]
print("前2行前3列：\n",sub_mat)

mat[1,2] = 999
print("修改(1,2)位置后的矩阵：\n",mat)