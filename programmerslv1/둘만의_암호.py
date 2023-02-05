'''
s
skip
index

문자열 s 의 각 알파벳을 index 만큼 뒤의 알파벳으로 바꿔준다 'abcdefghijklmnopqrstuvwxyz'
skip에 있는 알파벳은 위에서 제외한다.
'''

def solution(s, skip, index):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for i in skip:
        alphabet = alphabet.replace(i, '')

    for j in s:
        x = alphabet.index(j)
        idx = (x + index)%len(alphabet)
        answer += alphabet[idx]
    return answer


print(solution('aukks', 'wbqd', 5)) # happy