'''
모든 단어의 첫 문자가 대문자 그 외는 소문자

공백문자가 연속해서 나올 수 있다.
'''

# def solution(s):
#     answer = ''
#     string = list(s.split(' '))
#     print(string)
#     for i in string:
#
#         if i != '':
#             if i[0].isalpha():
#                 answer += ' '+i.capitalize()
#
#             else:
#                 answer += ' '+i.lower()
#
#         else:
#             answer += ' '
#
#     return answer.lstrip()





'''
## i.capaitalize() 공백에 대해서도 작동하므로.. 적당하다.
def solution(s):
    answer = ''
    for i in s.lower().split(' '):
        if answer == '':
            answer += i.capitalize()
        else:
            answer += ' '+i.capitalize()
    return answer
'''


print(solution("3people unFollowed me"))
print(solution("for the last week"))
print(solution('a   a   a   a   '))
print(solution('a   a   a   3w   '))