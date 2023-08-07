from collections import deque
import itertools


def solution(elements):
    tot = sum(elements)
    elements = deque(elements)
    answer = []
    for n in range(1, len(elements)//2 + 1):
        for _ in range(len(elements)):
            res = deque(elements, maxlen=n)
            answer.append(sum(res))
            answer.append(tot - sum(res))
            # print(answer)
            elements.rotate(1)
    answer.append(sum(elements))
    # print(set(answer))
    return len(set(answer))