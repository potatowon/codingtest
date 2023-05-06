import sys

t = int(input())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    max_value = max(a, b)
    min_value = min(a, b)
    while min_value != 0:
        max_value, min_value = min_value, max_value%min_value
    gcd = max_value
    print((a//gcd)*(b//gcd)*gcd)