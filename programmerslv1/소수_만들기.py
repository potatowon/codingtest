import itertools
def solution(nums):
    cnt = 0
    numbers = list(itertools.combinations(nums, 3))
    total = []
    for i in numbers:
        a = sum(i)
        total.append(a)

    m = max(total)
    primes = [False, False] + [True]*(m-1)
    for i in range(2, int(m**0.5)+1):
        if primes[i]:
            for j in range(i*2, m+1, i):
                primes[j] = False
    n = [i for i in range(m+1) if primes[i]]

    for k in total:
        if k in n:
            cnt +=1
    return cnt

print(solution([1,2,3,4]))
