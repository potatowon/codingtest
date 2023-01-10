# 삼각형의 완성 조건

'''
가장 긴변의 길이는 다른 두변의 길이의 합보다 작다

두변의 길이가 주어짐
1. 주어진 길이에서 max 값 정하기
2. 새로운 max 값쓰기
'''

def solution(sides):
    answer = []
    long_term = max(sides)
    i = long_term - min(sides) + 1
    j = max(sides)
    while (i + min(sides) > long_term) and (i < long_term):
        answer.append(i)
        i += 1

    while j < sides[0] + sides[1]:
        answer.append(j)
        j += 1
    return len(answer)

# test

print(solution([1,2]))
print(solution([3,6]))
print(solution([11,7]))
