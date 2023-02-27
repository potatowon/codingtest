import heapq
import sys

h = []
n = 0
while n != -1:
    n = int(sys.stdin.readline().strip())
    if n > 0 :
        heapq.heappush(h, -n)
    elif n == 0:
        if h:
            print(-1 * heapq.heappop(h))
        else:
            print(-1)
