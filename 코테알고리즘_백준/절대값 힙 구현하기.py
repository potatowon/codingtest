'''
실버 1 11286
절대값 힙

1. 배열에 정수 x(x != 0)을 넣는다
2. 배열에서 절대값이 가장 작은 값을 출력한 후 그 값을 배열에서 제거 한다. 
그 값이 여러개 일 경우 그 중 가장 작은 수를 출력하고 그 값을 배열에서 제거한다.

비어있는 배열에서 시작한다 절댓값 힙을 구현하시오.
'''

'''
애초에 넣을때 비교해 가면서 앞뒤로 넣어야 한다...
'''
import heapq as hp
import sys

pq = []

for _ in range(int(input())):
  x = int(sys.stdin.readline())
  if x:
    hp.heappush(pq, (abs(x), x))        # 절댓값 기준, 그다음 x 값 기준 min sort
    # print(pq)
  else:
    print(hp.heappop(pq)[1] if pq else 0)


'''
힙구조 -> 우선순위 큐 사용
'''