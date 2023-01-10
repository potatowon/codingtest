# 치킨 쿠폰
'''
치킨 10마리당 무료치킨 1마리 쿠폰 1장
100//10 = 10 0
10//10 = 1 0
11치킨

1081/10 = 108 1
109/10 = 10 9
19/10 = 1 9
10/10 = 1 0
1/10 = 0
120 치킨

27/10 = 2 7
9/10 = 0
'''
def solution(chickes):
    s = chickes
    answer = 0
    a =1
    while a != 0:
        a = s//10
        n = s%10
        s = a + n
        answer += a
    return answer


print(solution(1081))
print(solution(100))
