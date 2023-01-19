'''
N 개의 숫자가 주어지고, 주어진 숫자의 앞뒤를 뒤집은 후 만약 그 숫자가 소수이면 소수를 출력한다.

뒤집는 함수와 아닌 함수의를 반드시 작성하라
'''
#
# i = '2500'
# j = i[::-1]
# print(int(j))
# 뒤집는 함수
import sys
N = int(input())
x = list(map(int, sys.stdin.readline().split()))
# list 컴프리 핸션 https://velog.io/@jonsyou/Python-list-comprehension-%EC%95%88%EC%97%90-if-else
def reverse(x):
    strings = [str(i) for i in x]
    reverse_num = [i[::-1] for i in strings]
    numbers = [int(i) for i in reverse_num]
    return numbers
def isPrime(numbers):
    prime_number = []
    K = max(numbers)
    ch = [0]*(K+1)
    for i in range(2, K+1):
        if ch[i] == 0:
            prime_number.append(i)
            ch[i] += 1
            for j in range(i,K+1,i):
                ch[j] += 1
    for num in numbers:
        if num in prime_number:
            print(num, end=' ')

numbers = reverse(x)
answer = isPrime(numbers)





