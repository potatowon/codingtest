import sys

t = int(input())

for _ in range(2):
    case = sys.stdin.readline().split()
    for idx, c in enumerate(case):
        if idx == len(case) -1:
            print(c[::-1])
        else:
            print(c[::-1], end=' ')