from collections import defaultdict

N, X = map(int, input().split())
visitors = list(map(int, input().split()))
prefix_sum = [0]*(N+1)
initial = 0
for idx, num in enumerate(visitors):
    initial += num
    prefix_sum[idx+1] = initial

cum_visitor = defaultdict(int)

for i in range(N-X+1):
    cur = prefix_sum[i+X] -prefix_sum[i]
    cum_visitor[cur] += 1

max_day = max(cum_visitor.keys())
if max_day == 0:
    print("SAD")
else:
    print(max_day)
    print(cum_visitor[max_day])




