def dfs(numbers, tot, idx):
    global ans
    if idx >= n:
        return
    tot += numbers[idx] # tot 1번째 항을 더함
    if tot == s:
        ans += 1
    dfs(numbers, tot - numbers[idx], idx+1) # idx 번째 항을 빼고(즉 없앤경우)
    dfs(numbers, tot, idx+1) # idx 있는경우



n, s = map(int, input().split())
numbers = list(map(int, input().split()))
ans = 0
dfs(numbers, 0, 0)
print(ans)


