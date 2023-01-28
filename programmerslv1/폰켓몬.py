'''
해시

N마리의 폰켓몬 -<> N/2 가져가도 됨

같은 종류의 포켓몬은 같은 번호

[3, 1, 2, 3]

4마리중 2마리를 고르는 경우의수
최대한 다양한 수의 포켓몬을 가지고자 한다.

[1, 2]
[1, 3]
[2, 3]
[3, 3]

이경우 가질 수 있는 최대한의 종류는 2종류

따라서 최대한 많은 종류를 선택하는 방법을 찾아 그때의 종류 번호의 개수를 return
'''
# 폰켓몬의 종류는 20,000
# 1. 폰켓몬을 N 개중 N/2개 뽑는 경우 먼저
## 각 폰켓몬의 종류 번호를 key 값으로 주고, value 값을 모두 1로 통일 한 후 -> value 값의 합이 제일 큰 경우를 reture

import itertools
def solution(nums):
    r = len(nums)//2
    # perm = list(itertools.permutations(nums, r))
    # print(set(perm))
    # m = 0
    # for case in perm:
    #     res = {}
    #     for i in case:
    #         res[i] = 1
    #     answer = sum(res.values())
    #     if answer > m:
    #         m = answer
    # return m
    res = set(nums)
    if len(res) <= r :
        return len(res)
    else:
        return r
print(solution([3,3,3,2,2,2]))
a = [0]*10






