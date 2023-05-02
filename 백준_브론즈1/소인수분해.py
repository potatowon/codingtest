n = int(input())

primes = [False, False] + [True]*(n-1)

for i in range(int(n**0.5) + 1):
    if primes[i]:
        for j in range(i*2, n+1, i):
            primes[j] = False
numbers = [num for num in range(n+1) if primes[num]]

idx = 0
while n != 1:
    if n%numbers[idx] == 0:
        n = n//numbers[idx]
        print(numbers[idx])
    else:
        idx += 1
