import sys

k, n = map(int, input().split())
lanLines = [int(sys.stdin.readline()) for _ in range(k)]
lanLines.sort()


def check(ans):
    return sum([i // ans for i in lanLines])


def binarySearch(lanLines):
    start = 1  
    end = max(lanLines)
    result = 0

    while start <= end:
        mid = (start + end) // 2
        if n <= check(mid):
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result


print(binarySearch(lanLines))
