import sys
n = int(input())

for _ in range(n):
    n, *score = map(int, input().split())
    avg = sum(score)/n
    tmp = 0
    for i in score:
        if i > avg:
            tmp += 1
    print("{:.3f}%".format((tmp/n)*100))

