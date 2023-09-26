import sys


def cntShare(mid):
    cnt = 1
    ep = xi[0]
    for i in range(1, n):
        if xi[i] - ep >= mid:
            cnt += 1
            ep = xi[i]
    return cnt

def binarySearch(xi):
    l = 1
    r = max(xi)

    while l <= r:
        mid = (r + l) // 2
        if cntShare(mid) >= c:
            res = mid
            l = mid + 1
        else:
            r = mid - 1
    return res

n, c = map(int, input().split())
xi = [int(sys.stdin.readline()) for _ in range(n)]
xi.sort()

print(binarySearch(xi))



