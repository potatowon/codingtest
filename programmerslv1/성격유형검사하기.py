'''
4개의 지표

1번 R , T
2번 C , F
3번 J, M
4번 A, N

n개의 질문 -> 7가지의 선택지 매우비동의 ( 3, 2, 1, 0, 1, 2, 3) 매우동의

지표 왼쪽이 비동의 , 오른쪽의 동의
선택지

"AN"  -> 5

cho > 3
'''

def solution(survey, choices):
    answer = ''
    dic = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    mbti = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for sur, cho in zip(survey, choices):
        if cho < 4:
            mbti[sur[0]] += dic[cho]
        else:
            mbti[sur[1]] += dic[cho]
    # print(mbti)
    # 1번유형
    if mbti['R'] >= mbti['T']:
        answer += 'R'
    else:
        answer += 'T'
    # 2번 유형
    if mbti['C'] >= mbti['F']:
        answer += 'C'
    else:
        answer += 'F'
    # 3번 유형
    if mbti['J'] >= mbti['M']:
        answer += 'J'
    else:
        answer += 'M'

    # 4 번 유형
    if mbti['A'] >= mbti['N']:
        answer += 'A'
    else:
        answer += 'N'


    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 2, 3, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))