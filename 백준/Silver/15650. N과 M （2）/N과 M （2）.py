n, m = map(int, input().split())
numbers = [i for i in range(1, n+1)]
ans = []
def solution(depth, num):
    if depth == m:
        print(' '.join(map(str, ans)))
        return
    for i in num:
        ans.append(i)
        num = [j for j in range(1, n+1) if j > i]
        solution(depth+1, num)
        ans.pop()

solution(0, numbers)

