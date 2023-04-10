'''
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
'''
import sys

n = int(input())
# print(n)
for _ in range(n):
    cnt = 1
    stack = []
    answer = 0
    ox = list(sys.stdin.readline().strip())
    # print(ox)
    for i in ox:
        if stack and stack[-1] == 'O' and i == 'O':
            cnt += 1
            answer += cnt
        elif i == "X":
            answer += 0
            cnt = 1
        elif stack and stack[-1] != "O" and i == "O":
            answer += cnt
        elif stack == [] and i == "O":
            answer += cnt

        stack.append(i)
    print(answer)