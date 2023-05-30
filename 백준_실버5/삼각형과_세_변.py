'''
Equilateral :  세 변의 길이가 모두 같은 경우
Isosceles : 두 변의 길이만 같은 경우
Scalene : 세 변의 길이가 모두 다른 경우
Invalid : 삼각형의 조건을 만족하지 못함

- 삼각형의 조건

가장 긴 변의 길이 >= 나머지 두 변의 길이의 합
'''

import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if (a, b, c) == (0, 0, 0):
        break
    elif max(a, b, c) < ((a+b+c) - max(a, b, c)):
        if a == b and b == c:
            print('Equilateral')
        elif (a == b) or (b == c) or (c == a): # if elif 구문의 특성을 이용!
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print('Invalid')

