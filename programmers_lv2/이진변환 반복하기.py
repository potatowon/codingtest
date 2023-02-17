a = 143
b = bin(a)

print(int(b, 2))


'''
0,1 로 이루어진 문자열에 대한 이진 변환의 정의
1. x의 모든 0을 제거
2. x의 길이를 c 라고 하면 x를 'c 를 이진법으로 표현한 문자열'

[s = 1이진변환의 횟수, 제거된 0의 갯수]
'''

def solution(s):
    answer = [0, 0]
    while s != '1':
        answer[1] += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        answer[0] += 1
    return answer


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))