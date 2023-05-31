import sys

paper =[[0]*100 for _ in range(100)]

n = int(input())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for rdx in range(y, y+10):
        for cdx in range(x, x+10):
            paper[rdx][cdx] = 1
answer = 0

for row in range(len(paper)):
    answer += sum(paper[row])

print(answer)

