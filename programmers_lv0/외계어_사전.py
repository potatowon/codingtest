# dhlrPdj tkwjs

'''
알파벳 spell 과 외계어사전 dic
spell에 담긴 알파벳을 모두 한번씩 사용한 단어가 dic에 존재한다면 1, 아니면 2 Return
'''

''' 각 알파벳이 모두 있는가? -> and , count=1 왜? 한번씩만 사용하라고 했으니까'''

def solution(spell, dic):
    answer = 0
    for word in dic:
        if len(spell) == sum([1 for i in spell if word.count(i)==1]):
            return 1
    return 2

# test

print(solution(["p","o","s"],["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"],["def", "dww", "dzx", "loveaw"]))
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))