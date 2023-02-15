'''
구간합

N*N (x1, y1) ~ (x2, y2) 까지의 합을 구하시오

'''

import sys

n, m = map(int, sys.stdin.readline().split(' '))
matrix = [[0]*(n+1)]
for _ in range(n):
    row = [0] + list(map(int, sys.stdin.readline().split(' ')))
    matrix.append(row)
# 2차원 배열 합 만들기

D =[[0]*(n+1) for _ in range(n+1)] # 합 배열 초기화

for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + matrix[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split(' '))
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)