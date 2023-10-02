import sys

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
    # print(d)

    if (x1 == x2) and (y1 == y2):
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if (abs(r1-r2) < d and d < r1 + r2) :
            print(2)
        elif d == r1+r2 or d == abs(r1-r2):
            print(1)
        elif d > r1+r2 or d < abs(r1-r2):
            print(0)
