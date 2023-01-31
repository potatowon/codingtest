'''
1~k 점
사과 m 개
사과 1상자 가격 (최저점수 * m)
얻을 수 있는 최대 이익
이익이 없으면 0

'''

def solution(k, m, score):
    n = len(score)//m
    # box = [[] for _ in range(n)]
    score.sort(reverse=True)
    box = [score[i:i + m] for i in range(0, n * m, m)]
    res = 0
    # j=0
    # for i in score:
    #     j = j%n
    #     box[j].append(i)
    #     j += 1
    # print(box)
    for b in box:
       min_k = min(b[:m])
       res += min_k*m

    return res


    print(box)


print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))