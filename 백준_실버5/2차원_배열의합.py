# import sys
#
# n, m = map(int, input().split())
#
# board = []
#
# for _ in range(n):
#     board.append(list(map(int, sys.stdin.readline().split())))
#
# t = int(input())
#
# for _ in range(t):
#     i, j, x, y = map(int, sys.stdin.readline().split())
#     answer = 0
#     for row in range(i-1, x):
#         for col in range(j-1, y):
#             answer += board[row][col]
#     print(answer)

import sys

n, m = map(int, input().split())

# board 배열
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 누적 합 배열 초기화
prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

# 누적 합 배열 계산
for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix_sum[i][j] = board[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

# 쿼리 처리
t = int(input())
for _ in range(t):
    i, j, x, y = map(int, sys.stdin.readline().split())
    answer = prefix_sum[x][y] - prefix_sum[i-1][y] - prefix_sum[x][j-1] + prefix_sum[i-1][j-1]
    print(answer)
