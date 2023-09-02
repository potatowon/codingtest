# 완전 탐색 problem 2

import sys

N, M = map(int, input().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
answer = []
for col in range(N - 8 + 1):
    for row in range(M - 8 + 1):
        cntW = 0
        cntB = 0
        for r in range(col, col + 8):
            for c in range(row, row + 8):
                if (r+c)%2 == 0:
                    if board[r][c] != 'B':
                        cntB += 1
                    if board[r][c] != 'W':
                        cntW += 1
                else:
                    if board[r][c] != 'W':
                        cntB += 1
                    if board[r][c] != 'B':
                        cntW += 1
        answer.append(cntB)
        answer.append(cntW)

print(min(answer))

