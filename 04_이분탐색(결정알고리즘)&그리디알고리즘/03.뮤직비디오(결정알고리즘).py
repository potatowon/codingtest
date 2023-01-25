'''
총 N 개의 곡이 들어가는데, 라이브의 순서가 그대로 유지 되어야 한다.


N, M = N 개의 곡, M 개의 dvd
라이브에서 부른 곡의 길이가 분 단위로 주어진다.
각 dvd 에는 같은 용량으로 노래가 들어가야한다.

즉 N 개의 곡을 같은 합이 되도록 M 등분

최소 용량의 크기
'''

## 이진탐색 어떤걸 기준으로 할지가 가장 정하기 어려움!

## hint 전체 시간을 값으로 정하고 해보자

import sys

N, M = map(int, sys.stdin.readline().split())
music = list(map(int, sys.stdin.readline().split()))
maxx = max(music)
start = 0
end = sum(music)

def count_dvd(mid):
    cnt = 1
    sum_ = 0
    for x in music:
        if sum_ + x > mid:
            cnt += 1
            sum_ = x
        else:
            sum_ += x
    return cnt

while start <= end:
    mid = (start + end)//2
    # Count : 개의 곡을 다 저장하면 나오는 dvd 의 개수를 return
    if (mid >= maxx) and (count_dvd(mid) <= M) :
        res = mid
        end = mid - 1
    else:
        start = mid + 1


    break

