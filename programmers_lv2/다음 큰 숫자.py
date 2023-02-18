'''
n의 다음 큰 숫자
1. n 보다 큰 자연수
2. n을 2진수로 변환했을때의 1의 갯수와 같다
3. n은 1, 2를 만족하는 수중에 가장작은 수
N  = 1,000,000

'''

def solution(n):
    one_cnt = bin(n)[2:].count('1')
    next_n = n + 1

    while True:
        if bin(next_n)[2:].count('1') == one_cnt:
            return next_n
        else:
            next_n += 1



print(solution(78))
print(solution(15))
print(solution(123))

