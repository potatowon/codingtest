'''
첫글자 = x

x 와  == x 아닌 글자
-> 절반으로 나눔

나누고 난 뒤의 문자열에 대해서 반복

두 횟수가 다른데 읽을 글자가 없거나 남는 부분이 없으면 종료

분해한 문자열의 갯수를 return
'''
from collections import deque
def solution(s):
    answer = 0
    t = ["", 0, 0]
    for i in s:
        if t[0] == "":
            t[0] = i
            t[1] += 1
        else :
            if t[0] == i:
                t[1] += 1
            else :
                t[2] += 1
            if t[1] == t[2]:
                answer += 1
                t = ["", 0, 0]
    if t != ["", 0, 0]:
        answer += 1
    return answer


print(solution('banana')) # 3

print(solution('abracadabra')) # 6

print(solution('aaabbaccccabba')) # 3

