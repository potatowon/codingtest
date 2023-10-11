import sys

t = int(input())
for _ in range(t):
    num = int(input())
    people = [tuple(map(int, sys.stdin.readline().split())) for _ in range(num)]
    people.sort(key=lambda x: x[0])

    cnt = 1
    max_interview_rank = people[0][1]

    for _, interview_rank in people[1:]:

        if interview_rank < max_interview_rank:
            cnt += 1
            max_interview_rank = interview_rank

    print(cnt)
