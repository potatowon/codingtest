## 파이썬에서 heap구현은 모듈을 이용하는 것이다.

import heapq

# heapq 모듈은 min heap

# heappush - 요소추가 

heap = []

heapq.heappush(heap, 45)
heapq.heappush(heap, 36)
heapq.heappush(heap, 54)
heapq.heappush(heap, 27)
heapq.heappush(heap, 63)
## array(27, 36, 45, 54, 63)

# heappop - 요소 제거

print(heapq.heappop(heap)) # 27
print(heapq.heappop(heap)) # 36
print(heapq.heappop(heap)) # 45


# heapreplace - 요소 '제거' 후 추가
heapq.heapreplace(heap, 10) # 54 가 제거되고 10 추가
print(heap[0]) # 10
## array(10, 63)


# heappushpop 요소 "추가" 후 제거하기

heapq.heappushpop(heap, 5) # 5 추가 하고 제거
print(heap[0]) # 10
## array(63)
