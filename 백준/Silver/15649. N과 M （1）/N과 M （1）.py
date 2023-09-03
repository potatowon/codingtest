n, m = map(int, input().split())
numbers = [i for i in range(1, n+1)]
res = []
ans = []
def backTraking(depth, numbers):
    if depth == m:
        print(' '.join(map(str, ans)))
        return
    for i in numbers:
        ans.append(i)
        new_num = [j for j in numbers if j != i]
    
        backTraking(depth+1, new_num)
        ans.pop()
backTraking(0, numbers)
