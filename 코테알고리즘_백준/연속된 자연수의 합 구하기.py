'''
어떤 자연수를 연속된 자연수의 합으로 나타내는 가짓수를 알고 있다.

예제
n = 15
1+2+3+4+5
4+5+6
7+8
15

4가지
'''


import sys

n = int(sys.stdin.readline())


start_idx, end_idx = 1, 1
cnt = 1
sum_ = 1


while end_idx != n:

    if sum_ == n:
       cnt += 1
       end_idx += 1
       sum_ += end_idx
    elif sum_ < n:
        end_idx += 1
        sum_ += end_idx
    else:
        sum_ -= start_idx
        start_idx += 1

print(cnt)


'''
프로그래머스 - 숫자의 표현 (비슷한 문제) ; 프로그래머스는 정답이지만, 백준은 메모리 초과

def solution(n):
    numbers = [i for i in range(n+1)]

    start_idx, end_idx = 1, 1
    cnt = 1


    while end_idx != n:
        sum_ = sum(numbers[start_idx:end_idx+1])

        if sum_ == n:
            cnt += 1
            end_idx += 1
        elif sum_ < n:
            end_idx += 1
        else:
            start_idx += 1
    return cnt

'''