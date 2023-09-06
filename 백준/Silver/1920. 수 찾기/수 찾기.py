import sys

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
m = int(input())
search = list(map(int, input().split()))

for i in search:
    ans = False
    right = 0
    left = n - 1
    while right <= left:
        mid = (right + left) // 2
        if numbers[mid] == i:
            ans = True
            break
        if numbers[mid] < i:
            right = mid + 1
        elif numbers[mid] > i:
            left = mid - 1
    if ans:
        print(1)
    else:
        print(0)