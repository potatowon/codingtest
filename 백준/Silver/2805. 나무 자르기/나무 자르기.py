def cutTree(trees, mid):
    ans = 0
    for i in trees:
        if i - mid >= 0:
            ans += (i - mid)
    return ans


def binarysearch(trees):
    r = trees[-1]
    l = 0
    res = 0
    while l <= r:
        mid = (r + l)//2
        rT = cutTree(trees, mid)
        if rT >= m:
            res = mid
            l = mid + 1
        elif rT < m:
            r = mid -1
    return res

n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
# print(trees)
print(binarysearch(trees))




