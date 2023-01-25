''' 자릿수 별로 합산 하시오'''

def solution(n):
    sum_ = 0
    for i in str(n):
        sum_ += int(i)

    return sum_