def consult(day):
    # 기본 종료 조건: day가 N을 초과하면 0을 반환
    if day > N:
        return 0
    
    # 상담을 하지 않는 경우와 상담을 하는 경우 중에서 최대 이익을 선택
    # 단, 상담을 할 경우, day + time[day] 이전의 날짜에는 상담을 할 수 없으므로 주의
    not_take = consult(day + 1)
    
    if day + time[day] <= N + 1:
        take = profit[day] + consult(day + time[day])
        return max(take, not_take)
    else:
        return not_take

N = int(input())
time, profit = [0], [0]

for _ in range(N):
    t, p = map(int, input().split())
    time.append(t)
    profit.append(p)

print(consult(1))
