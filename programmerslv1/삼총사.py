'''
각자의 정수번호를 가지고 있고, 그 정수들의 합이 0이 되는 3명을 삼총사라 한다.

정수 배열이 주어졌을 때, 만들 수 있는 삼총사의 경우의 수를 구하시오.

정수 배열에서 순서 상관없이 3명을 뽑은 배열을 만든다 -> combination
'''
import itertools


# a = [-2, 3, 0, 2, -5]
#
# import itertools
#
# b = list(itertools.combinations(a, 3))
# for i in b:
#     if sum(i) == 0:
#         print('삼총사')

def solution(number):
    comb = list(itertools.combinations(number, 3))
    cnt = 0
    for i in comb:
        if sum(i) == 0:
            cnt += 1
    return  cnt