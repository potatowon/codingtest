'''

구명보트를 최대한 적게 사용하여 모든 사람을 구출하고자 한다.

n <= 50,000

'''
from collections import deque
def solution(people, limit):
    cnt = 0
    people.sort()
    people = deque(people)
    while people:
        if len(people) == 1:
            people.pop()
            cnt += 1

        elif people[0] + people[-1] > limit:
            people.pop()
            cnt += 1

        elif len(people) >= 2:
            people.pop()
            people.popleft()
            cnt += 1

    return cnt


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([50], 60))