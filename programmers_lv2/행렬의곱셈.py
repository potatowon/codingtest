def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr2[0])
    p = len(arr2)

    result = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(p):
                result[i][j] += arr1[i][k] * arr2[k][j]

    return result

# print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))


