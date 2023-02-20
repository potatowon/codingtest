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

numbers = [i for i in range(16)]

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

print(cnt)



