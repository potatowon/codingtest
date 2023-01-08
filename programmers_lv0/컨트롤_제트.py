# 컨드롤 제트

'''
문자열의 전부 합을 구하되 'Z'가 주어진 경우 앞 문자열을 다시 뺀다
문자열은 공백으로 나누어져 있다.
'''

def solution(s):
    answer = 0
    strings = s.split(' ')
    for idx in range(len(strings)):
        if strings[idx] == 'Z':
            answer -= int(strings[idx-1])
        else:
            answer += int(strings[idx])
    return answer

# test

print(solution("1 2 Z 3"))
print(solution("10 Z 20 Z 1"))
print(solution("10 Z 20 Z"))
print(solution("-1 -2 -3 Z"))