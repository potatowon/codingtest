'''
F(n) = F(n-1) + F(n-2)
'''


def solution(n):
    answer = 0
    F = [0, 1] + [0]*(n-1)

    for i in range(2, n+1):
        F[i] = F[i-1]+F[i-2]
    return F[n]%1234567

print(solution(5))