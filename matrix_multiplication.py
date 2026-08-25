def matrix_chain_order(dims):
  
    n = len(dims) - 1         
    if n < 2:
        return 0
    m = [[0] * n for _ in range(n)]


    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = (m[i][k] + m[k+1][j] +
                        dims[i] * dims[k+1] * dims[j+1])
                if cost < m[i][j]:
                    m[i][j] = cost
    return m[0][n-1]


dims = [10, 30, 5, 60]
print("Minimum scalar multiplications:", matrix_chain_order(dims))
