'''
공백을 기준으로나눈다.
'''

def solution(s):
    answer = s.split(' ')
    result = []
    for i in answer:
        res = ''
        for j in range(len(i)):
            if j%2 == 0:
                res += i[j].upper()
            else:
                res += i[j].lower()
        result.append(res)
    # print(' '.join(result))
    return ' '.join(result)


print(solution("try hello world"))
