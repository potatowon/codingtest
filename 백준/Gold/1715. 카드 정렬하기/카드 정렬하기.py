import heapq
import sys

N = int(input())
hq = []
for _ in range(N):
    num = int(sys.stdin.readline())
    heapq.heappush(hq, num)
answer = 0

while len(hq) != 1:
    first = heapq.heappop(hq)
    second = heapq.heappop(hq)
    tot = first + second
    answer += tot
    heapq.heappush(hq, tot)

print(answer)