n = int(input())

MOD = 1000000

def matmul_matrix(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    assert cols_A == rows_B

    result = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= MOD
    return result

def matrix_power(mat, exponent):
    if exponent == 1:
        return mat
    res = [[1, 0], [0, 1]] # identity matrix
    while exponent:
        if exponent & 1:
            res = matmul_matrix(res, mat)
        mat = matmul_matrix(mat, mat)
        exponent >>= 1
    return res

M = [[1, 1], [1, 0]]
result_matrix = matrix_power(M, n-1)
print(matmul_matrix(result_matrix, [[1], [0]])[0][0] % MOD)
