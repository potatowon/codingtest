'''
가격이 떨어지지 않는 시간은 몇초인지 return
'''
from collections import deque

def solution(prices):
    prices = deque(prices)
    idx = 0
    answer = [0]*len(prices)            # 각 인덱스별 시간 초기화
    while prices:
        now = prices.popleft()
        for i in prices:
            answer[idx] += 1            # 한 텀이라도 넘어가면 1초라고 경과되므로 사용한다.
            if now <= i:                # 감소하지 않았으면 pass
                pass
            else:                       # 감소한 경우 바로 for 문을 중지 시킨다.
                break
        idx += 1                        # 다음 인덱스에 대한 계산을 이어 나간다.

    return answer



print(solution([1,2,3,2,3]))