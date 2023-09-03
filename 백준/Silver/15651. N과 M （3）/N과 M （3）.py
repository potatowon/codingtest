n, m = map(int, input().split())
answer = []

def backTraking(depth):
    if depth == m:
        print(' '.join(map(str, answer)))
        # print('return 합니다~~~~~~~')
        return
    for i in range(1, n+1):
        answer.append(i)
        # print(answer, '더하기')
        backTraking(depth + 1)
        # print(answer, '재귀 후')
        answer.pop()
        # print(answer, ' Pop 후')

backTraking(0)