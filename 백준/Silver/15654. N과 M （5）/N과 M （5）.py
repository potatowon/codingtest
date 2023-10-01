import sys

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
ans = []
def solution(depth, numbers):
    if depth == m:
        print(' '.join(map(str, ans)))
    for i in numbers:
        ans.append(i)
        num = [j for j in numbers if j != i]
        solution(depth+1, num)
        ans.pop()

solution(0, numbers)