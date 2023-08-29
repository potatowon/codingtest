import sys
from collections import  defaultdict
t = int(input())

for _ in range(t):
    fashions = defaultdict(list)
    n = int(sys.stdin.readline())
    for _ in range(n):
        name, kind = sys.stdin.readline().rstrip().split()
        fashions[kind].append(name)

    ans = 1
    for k, v in fashions.items():
        ans *= (len(v) + 1)

    print(ans - 1)

