import sys

t = int(input())

for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    apt = [[0]*n for _ in range(k+1)]
    for j in range(k+1):
        answer = 0
        for i in range(n):
            if j == 0:
                apt[j][i] = i+1
            else:
                answer += apt[j-1][i]
                apt[j][i] = answer
    print(apt[k][n-1])
