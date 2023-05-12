import sys

t = int(input())

for _ in range(t):
    answer = []
    n = int(input())
    for _ in range(n):
        name, alcohol = sys.stdin.readline().split()
        answer.append((name, int(alcohol)))
    (max_val, max_name) = answer[0][1], answer[0][0]

    for i in answer:
        if i[1] >= max_val:
            max_val = i[1]
            max_name = i[0]
    print(max_name)