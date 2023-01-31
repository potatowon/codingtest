'''
매일 1명씩 노래 -> 점수 부여

상위 k 번째 이내면 명예의 전당에 올려 기념
-> k 번째 일까지는 다 등록
그 이 후는 밀어내기 시작
명예의 전당의 최하위 점수를 발표한다.

k : 명예의 전당의 목록의 개수
score : 점수
'''

def solution(k, score):
    answer = []
    p = []
    for idx in range(len(score)):

        if idx < k:
            p.append(score[idx])
            min_p = min(p)
            answer.append(min_p)
        else:
            p.sort()
            if score[idx] > p[0]:
                p.pop(0)
                p.insert(0, score[idx])
                min_p = min(p)
                answer.append(min_p)
            else:
                min_p = min(p)
                answer.append(min_p)

    return answer


print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])) #[0, 0, 0, 0, 20, 40, 70, 70, 150, 300]

