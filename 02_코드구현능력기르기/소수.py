'''
제한 시간 1초

N이 입력되면 N까지의 소수를 입력하는 프로그램을 만드시오
'''

'''
run time error
'''
#
# import sys
#
# N = int(sys.stdin.readline())
#
# # 소수란 1, 자기자신만을 약수로 가지는 수를 의미한다. 즉, 1과 자기자신만으로 나누어지는 숫자를 찾아야한다.
# sosu = []
# for number in range(1, N+1):
#     division = []
#     for i in range(1, number+1):
#         if number%i == 0:
#             division.append(i)
#     if len(division) == 2:
#         sosu.append(number)
# print(len(sosu))

## 소수의 개수를 구하기 - 에라토스테네스 체 사용해서 다시 해보자ㅇ

import sys

N = int(sys.stdin.readline())
ch = [0]*(N+1)
prime_number = []
for i in range(2, N+1):

    if ch[i] == 0:
        prime_number.append(i)
        ch[i] += 1
        for j in range(i,N+1,i):
            ch[j] += 1
print(len(prime_number))
''' 에라토스테네스의 체'''

# num 까지의 소수를 구하는 방법
# def get_primes(num):
#     prime = [False, False] + [True]*(num-1)
#     for i in range(2, int(num**0.5)+1):
#         if prime[i]:
#             for j in range(i*2, num+1, i):
#                 prime[j] = False
#
#     return [i for i in range(num) if prime[i]]

