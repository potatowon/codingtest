import sys


def max_profit(n, prices):
    # 뒤에서부터 시작하기 때문에 마지막 날의 주가를 최대 주가로 초기화
    max_price_from_behind = prices[-1]
    profit = 0 # 이익을 저장하는 변수

    # 뒤에서부터 앞으로 순회
    for i in range(n-2, -1, -1): # n-2에서 시작해서 0까지 -1씩 감소하며
        # 현재 주가가 이후의 최대 주가보다 높다면, 그 값을 최대 주가로 갱신
        if prices[i] > max_price_from_behind:
            max_price_from_behind = prices[i]
        else:
            # 현재 주가가 이후의 최대 주가보다 낮다면 그 차이만큼 이익으로 계산
            profit += max_price_from_behind - prices[i]

    return profit

T = int(input())
for _ in range(T):
    n = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().split()))
    print(max_profit(n, prices))

