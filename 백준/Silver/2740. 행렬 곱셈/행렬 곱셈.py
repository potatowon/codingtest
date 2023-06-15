import sys

n, m_1 = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

m_2, k = map(int, sys.stdin.readline().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(m_2)]
C = [[0]*k for _ in range(n)]
for s in range(n):
    for t in range(k):
        ans = 0
        for r in range(m_1):
            ans += A[s][r]*B[r][t]
        C[s][t] = ans


for i in C:
    print(*i)