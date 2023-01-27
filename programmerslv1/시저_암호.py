'''
문장의 알파벳을 거리만큼 밀어서 다른 알파벳으로 만든다.

'''
#
def solution(s, n):
    answer = ''
    s_alpha = 'abcdefghijklmnopqrstuvwxyz'*2
    l_alpha = (s_alpha.upper())
    for i in s:
        if i.isupper():
            answer += l_alpha[l_alpha.index(i) + n]
        elif i.islower():
            answer += s_alpha[s_alpha.index(i) + n]
        else:
            answer += ' '
    return answer
