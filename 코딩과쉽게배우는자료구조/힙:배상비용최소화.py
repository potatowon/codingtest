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
    ## 예외에 대한 제거
    if sum(works) <= no:
        return 0
    max_heap = []
    for i in works:
        heapq.heappush(max_heap, (-i))   # 파이썬의 heap 구조는 min heap 이므로 (-val, val) 방법을 이용한다. 
                                            # 다만 해당 문제의 경우 **2 으로 답을 도출하는 바 -i a만 써도 무방
    for _ in range(no):
        heapq.heapreplace(max_heap, max_heap[0] + 1) # replace는 제거 후 추가. 
    result = 0
    # for i in max_heap:
    #     result += i[1]**2
    # result = 0
    return sum([i ** 2 for i in max_heap])

print(solution(4, [4, 3, 3]))
print(solution(2, [2,3]))