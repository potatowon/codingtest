import sys
t = int(input())
res = []
for _ in range(t):
    res.append(sys.stdin.readline().rstrip())
res = set(res)
res = list(res)
res.sort(key=lambda x : (len(x), x))
for r in res:
    print(r)
