# 가장 큰애를 계속 뽑아서 n==0 될때까지 -1 해보자
import heapq

def solution(n, works):
    
    if sum(works) <= n:
        return 0
    heap = []
    for i in works:
        heapq.heappush(heap, -i)
    cnt = 0
    for _ in range(n):
        a = heapq.heappop(heap)
        a += 1
        heapq.heappush(heap, a)
    
    answer = 0
    for i in heap:
        answer += i**2
    return answer