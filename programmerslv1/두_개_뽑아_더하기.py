'''
서로 다른 인덱스에 있는 두개의 수를 뽑아 더해서 만들 수 있는 모든 수의 배열을 오름차순으로 담아내시오
'''

import itertools

def solution(numbers):
    answer = []
    res = list(itertools.permutations(numbers, 2))

    for i in res:
        answer.append(sum(i))
    # answer = set(answer)
    # answer = list(answer)
    # answer.sort()
    return sorted(list(set(answer)))

print(solution([2,1,3,4,1]))
