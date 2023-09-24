import sys


def gcd(a, b):
    if a < b:
        b, a = a, b
    if a%b: return gcd(b, a%b)
    else: return b

def lcm(a, b):
    G = gcd(a, b)
    return G * (a // G) * (b //G)

t = int(input())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b))