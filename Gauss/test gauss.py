import numpy as np

A = np.array([[1, 2], [3, 4]])
b = np.array([[5], [6]])
B = np.array([[9, 8], [7, 6]])
t = np.zeros((2, 2))
z = []
for i in range(A.shape[0]):
    for k in range(A.shape[1]):
        t[i, k] = A[i, k] + B[i, k]
        z.extend([A[i, k] + B[i, k]])
print(t)
print(z)

s = np.append([[1]], [[3]], axis=0)
#s = np.array([[1, 4, 7]])
print(s.shape)

# A=np.array([1, 2, 3, 4])
# B=A[np.newaxis,:]
# C=A[:,np.newaxis]
# print(A)
# print(A.shape)
# print(B)
# print(B.shape)
# print(C)
# print(C.shape)
# D=
# print(D)
# print(D.shape)
# print(len(D))
