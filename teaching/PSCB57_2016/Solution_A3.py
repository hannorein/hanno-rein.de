from numpy.linalg import solve
def s(A,v):
    return solve(A,v)
def lsf(x,y,f):
    N = len(x)
    M = len(f(x[0]))
    C = []
    for i in range(N):
        C.append(f(x[i]))
    b = [0. for i in range(M)]
    for j in range(M):
        for i in range(N):
            b[j] += C[i][j]*y[i]
    A = [[0. for j in range(M)] for i in range(M)]
    for j in range(M):
        for i in range(M):
            for k in range(N):
                A[i][j] += C[k][i]*C[k][j]
    return s(A,b)
