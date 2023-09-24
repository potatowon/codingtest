n, k = map(int, input().split())
def factorial(base):
    ans = 1
    for i in range(1, base+1):
        ans *= i
    return ans
print((factorial(n) // (factorial(n-k)*factorial(k)))%10007)