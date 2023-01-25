'''
각 마구간은 좌표를 가지며, 좌표가 중복될 일은 없다.



C 마리의 말을 N 개의 마구간에 배치 가장 가까운 두 말의 거리 출력
'''

import sys

N, C = map(int, sys.stdin.readline().split()) # 마구간 수와 말의 수
xi = [int(sys.stdin.readline()) for _ in range(N)] # N 개에 걸친 마구간의 좌표
xi.sort()


start = 1
end = max(xi)
def count_horse(mid):
    cnt = 1
    ep = xi[0]
    for i in range(1, N):
        if xi[i] - ep >= mid:
            cnt += 1
            ep = xi[i]
    return cnt


while start <= end:
    mid = (start + end)//2
    if count_horse(mid) >= C:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)
