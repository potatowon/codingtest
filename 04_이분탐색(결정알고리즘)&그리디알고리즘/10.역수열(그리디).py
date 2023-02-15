'''
1 부터 n 까지의 수를 한번씩만 사용하여 이루어진 수열(즉, 중복은 없다)
각각의 수 앞에 놓여 있는 자신보다 큰 수들의 개수를 수열로 표현한것

4 8 6 2 5 1 3 7

역수열
5, 3, 4, 0, 2, 1, 1, 0
역수열이 주어졌을때 원래의 수열을 구하여라

자연수 n
역수열

원래수열 * 로 출력
'''

import sys

n = int(sys.stdin.readline())
re_num = list(map(int, sys.stdin.readline().split()))

numbers = [i for i in range(1, n+1)]
numbers.reverse()
re_num.reverse()
result = []
for n, r in zip(numbers, re_num):
    result.insert(r, n)
print(*result)