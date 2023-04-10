n = int(input())
numbers = list(map(int, input().split()))
num = 1000

prime = [False, False] + [True]*(num-1)


for i in range(2, int(num**0.5)+1):
    if prime[i]:
        for j in range(i*2, num+1, i):
            prime[j] = False
    
primes = [i for i in range(num+1) if prime[i]]
cnt = 0

for i in numbers:
    if i in primes:
        cnt += 1

print(cnt)