from collections import deque
n, k = map(int, input().split())

numbers = deque([i for i in range(1, n+1)])
ans = []
while numbers:
    idx = 1
    while idx < k:
        a = numbers.popleft()
        numbers.append(a)
        idx += 1
    ans.append(numbers.popleft())
ans = map(str, ans)
print('<' + ', '.join(ans) + ">")