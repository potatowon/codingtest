import sys
import heapq
n = int(input())
hq = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if hq:
            print(-heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq, -x)

