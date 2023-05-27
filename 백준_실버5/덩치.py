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



## contiune, break, pass 의 차이
'''
pass : 실행할 코드가 없는 것으로 다음 행동을 진행
continue : 바로 다음 순번의 loop 진행
break : 반복문을 멈추고 loop 밖으로 탈출
'''