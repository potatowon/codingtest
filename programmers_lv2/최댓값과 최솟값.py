'''
공백으로 구분되어진 s중 str(max min) 구하시오
'''

def solution(s):
    num = list(map(int, s.split(' ')))
    answer = str(min(num))+' ' +str(max(num))
    return answer

print(solution('1 2 3 4'))
print(solution('-1 -2 -3 -4'))
print(solution('-1 -1'))