n, m = map(int, input().split())
ans = []
numbers = [i for i in range(1, n+1)]

def solution(depth, numbers):
    if depth == m:
        print(' '.join(map(str, ans)))
        return
    for i in numbers:
        ans.append(i)
        num = [j for j in numbers if j >= i]

        solution(depth+1, num)
        ans.pop()

solution(0, numbers)