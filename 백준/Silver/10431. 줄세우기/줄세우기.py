import sys

P = int(input())
for _ in range(P):
    res = []
    t, *num = map(int, input().split())
    answer = 0
    for i in num:
        res.append(i)
        new_num = sorted(res)
        if new_num != res:
            answer += res.index(i) - new_num.index(i)
        res.sort()
    print(t, answer)