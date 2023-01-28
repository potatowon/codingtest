'''
a : 마트에 주어야하는 병 수
b : 주는 콜라수
n : 지금 가지고 있는 병 수
'''

def solution(a, b, n):
    answer = 0
    m = n
    while True:
        s = (m//a)*b
        r = m%a
        answer += s
        m = s + r
        if m < a:
            break
    return answer
print(solution(3,1,20))