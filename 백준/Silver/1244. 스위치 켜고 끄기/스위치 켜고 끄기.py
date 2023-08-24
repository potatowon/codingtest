import sys
def flip_switch(switches, center):
    left, right = center - 1, center + 1

    # 중심을 기준으로 좌우로 확장하며 대칭 확인
    while left >= 0 and right < len(switches) and switches[left] == switches[right]:
        left -= 1
        right += 1

    # 대칭이 아닌 경우 확장 멈추고 지금까지의 범위의 스위치 상태 변경
    for i in range(left + 1, right):
        switches[i] = 1 - switches[i]  # 0은 1로, 1은 0으로 변경

    return switches

N = int(input())
switch = list(map(int, input().split()))
n_student = int(input())
for _ in range(n_student):
    sex, num = map(int, sys.stdin.readline().split())
    if sex == 1:
        for i in range(num, N+1, num):
            if switch[i-1]:
                switch[i-1] = 0
            else:
                switch[i-1] = 1
        # print(switch)
    else:
        switch = flip_switch(switch, num-1)
        # print(switch)

for i in range(0, len(switch), 20): # 0부터 시작하여 20개 간격으로 인덱스 추출
    print(*switch[i:i+20])
