'''
갑옷의 재료들은 고유한 번호가 있고, 고유 번호를 합쳐서 M 이되면 갑옷이 만들어진다

N개의 재료와 M이 주어졌을때 몇 개의 갑옷을 만들 수 있는지 
'''

import sys

n = int(input())

m = int(input())

numbers = list(map(int, sys.stdin.readline().split(' ')))
numbers.sort()
# [1, 2, 3, 4, 5, 7]
start_idx = 0
end_idx = n-1
cnt = 0

while start_idx < end_idx:
    sum_ = numbers[start_idx] + numbers[end_idx]
    if sum_ > m:
        end_idx -= 1
    elif sum_ < m:
        start_idx += 1
    else:
        cnt += 1
        start_idx += 1
        end_idx -= 1
print(cnt)

