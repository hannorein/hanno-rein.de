A = [[2.,  1.,  4.,  1.],
     [3.,  4., -1., -1.],
     [1., -4.,  1.,  5.],
     [2., -2.,  1.,  3.]]

v = [-4., 3., 9., 7. ]

N = len(v)

# Gaussian elimination
for m in range(N):
    div = A[m][m] 
    for n in range(N):
        A[m][n] /= div
    v[m] /= div
    for l in range(m+1,N):
        mult = A[l][m]
        for o in range(N):
            A[l][o] -= mult*A[m][o]
        v[l] -= mult*v[m]

# Backsubstitution
x = [0 for i in range(N)]
for m in range(N-1,-1,-1):
    x[m] = v[m]
    for l in range(m+1,N):
        x[m] -= A[m][l]*x[l]

print(x)


# Using numpy:
A = [[2.,  1.,  4.,  1.],
     [3.,  4., -1., -1.],
     [1., -4.,  1.,  5.],
     [2., -2.,  1.,  3.]]

v = [-4., 3., 9., 7. ]
import numpy 
print(numpy.linalg.solve(A,v))
