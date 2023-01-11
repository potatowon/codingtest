# 등수 매기기
## 진료 순서 정하기와 같은 풀이
'''

'''

def solution(score):
    avgs = []
    for data in score:
        avgs.append(sum(data)/len(data))
    sort_avgs = sorted(avgs, reverse=True)
    answer = [sort_avgs.index(avg)+1 for avg in avgs]
    return answer

print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))