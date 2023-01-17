# 연속된 숫자의 합

'''
num개의 연속된 숫자의 합이 total이 되는 num개의 원소를 지닌 list 를 return 하시오

N 부터 연속된 num 개의 list 의 합

N, N+1, N+2, ... , N+(num-1)
total = num*N + sum(0~(num-1))
N = (total - sum(0~ num-1))//num
-> N 부터 시작된 num개의 list
'''

def solution(num, total):
    n =int((total - sum([i for i in range(num)]))/num)
    answer = []
    for j in range(num):
        answer.append(n+j)
    return answer