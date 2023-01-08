# 문자열 계산하기

'''
문자열로 된 수식 계산하기
'''

def solution(my_string):
    strings = my_string.split(' ')
    answer = int(strings[0])
    print(my_string)
    for string_idx in range(len(strings)):

        if strings[string_idx] == '+':
            answer += int(strings[string_idx+1])
        elif strings[string_idx] == '-':
            answer -= int(strings[string_idx+1])
        else:
            pass
    return answer

# test
print(solution("3 + 4"))