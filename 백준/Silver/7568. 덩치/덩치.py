import sys

n = int(input())
lst = [tuple((map(int, sys.stdin.readline().split()))) for _ in range(n)]
rank_lst = []
for idx in range(len(lst)):
    rank = 1
    tall = lst[idx][1]
    weight = lst[idx][0]
    for jdx in range(len(lst)):
        if idx == jdx:
            continue
        elif tall < lst[jdx][1] and weight < lst[jdx][0]:
            rank += 1
        elif tall > lst[jdx][1] or weight > lst[jdx][0]:
            pass

    rank_lst.append(rank)
print(*rank_lst)
