'''
M 이상 N 이하의 소수를 찾고

소수의 합과 최솟값을 출력하라
'''


m = int(input())
n = int(input())

primes = [False, False] + [True]*(n-1)

for i in range(2, int(n**0.5)+1):
    if primes[i]:
        for j in range(i*2, n+1, i):
            primes[j] = False

answer = []
for i in range(m, n+1):
    if primes[i]:
        answer.append(i)

if answer:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)
