def solution(n):
    primes = [False, False] + [True]*(n-1)
    for i in range(int(n**0.5)+1):
        if primes[i]:
            for j in range(i*2, n+1, i):
                primes[j] = False
    answer = [i for i in range(n+1) if primes[i]]
    return len(answer)


print(solution(10))