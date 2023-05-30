import sys

T = int(input())

def factorial(n):
    ans = 1
    if n == 0:
        return ans
    while n != 1:
        ans *= n
        n -= 1
    return ans

# print(factorial(3))

for _ in range(T):
    r, n = map(int, sys.stdin.readline().split())
    print( factorial(n) // (factorial(r) * factorial(n-r)))

