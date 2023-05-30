import sys

n = int(input())
ax = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    ax.append((x, y))

ax.sort(key=lambda x : (x[1], x[0]))
for x, y in ax:
    print(x, y)