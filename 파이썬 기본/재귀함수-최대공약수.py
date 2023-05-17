## 유클리드 호제법

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

## smaller
def gcd(a, b):
    smaller = min(a, b)
    while True:
        if (a%smaller == 0 and b%smaller==0):
            return smaller
        else:
            smaller -= 1

print(gcd(10, 4))