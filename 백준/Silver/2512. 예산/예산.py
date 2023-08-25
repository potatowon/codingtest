N = int(input())
budgets = list(map(int, input().split()))
tot_budget = int(input())


left, right = 0, max(budgets)

while left <= right:
    mid = (left + right) // 2
    total = sum(min(b, mid) for b in budgets) 
    if total > tot_budget:
        right = mid - 1
    else:
        left = mid + 1

print(right)
