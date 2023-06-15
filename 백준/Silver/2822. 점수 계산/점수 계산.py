import sys

score = [(idx+1, int(sys.stdin.readline())) for idx in range(8)]
score.sort(key=lambda x : x[1], reverse=True)

res_score = 0
res_q = []

for q, s in score[:5]:
    res_score += s
    res_q.append(q)
res_q.sort()
print(res_score)
print(*res_q)
