import sys

n = int(input())
res = []
for _ in range(n):
    n,m = map(int, sys.stdin.readline().split())
    res.append((n, m))
res.sort(key=lambda x: (x[0], x[1]))
for i in res:
    print(*i)