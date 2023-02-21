'''
n편의 논문 중, h 번 이상 인용된 논문이, h편 이상/ 나머지는 논문이 h 번이하 인용되었다면

h의 최댓값이 이 과학자의 h-index 입니다.

논문의 인용횟수가 주어졌을때 h-index return
'''

def solution(citations):
    citations.sort()
    ref_max = citations[-1]

    while True:
        cnt = 0
        for i in citations:
            if i >= ref_max:
                cnt += 1
        if ref_max <= cnt:
            return ref_max
        else:
            ref_max -= 1

print(solution([3, 0, 6, 1, 5]))




