'''
배상 비용 += 남은일의 작업량**2
n = 4, work = 4, 3, 3 일때 배상비용을 최소화 하기 위해
일한 결과는 [2, 2, 2]
이므로 배상비용은 2**2 + 2**2 + 2**2 이다.

n <= 1,000,000
work < 1,000
각 작업량 1,000 이하 자연수



ex n = 4 [2, 3, 3]

[0 2 2] -> 4 # 문제는 기한 내에 완성하지 못함을 전제로 하므로 계산 후 0 이되는 것은 고려 하면 안된다.
[1 1 2] -> 6 # 즉 이경우의 수가 배상비용이 최소화 되는 경우다

따라서 최소값을 구하는 방법은 각 배열에서 최대값을 빼 1씩 빼는 것을 N 번 만큼 반복하면 된다.
'''
import heapq

def solution(no, works):
    
    max_heap = []
    for i in works:
        heapq.heappush(max_heap, (-i, i))   # 파이썬의 heap 구조는 min heap 이므로 (-val, val) 방법을 이용한다.
    for _ in range(no):
        w_max_n, w_max_p = heapq.heappop(max_heap)
        w_max_n += 1
        w_max_p -= 1
        heapq.heappush(max_heap, (w_max_n, w_max_p))
    result = 0
    for i in max_heap:
        result += i[1]**2
    # result = 0
    return result

print(solution(4, [4, 3, 3]))
print(solution(2, [2,3]))