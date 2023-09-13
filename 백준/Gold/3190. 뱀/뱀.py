from collections import deque
import sys

def direction_chage(d, c):
    if c == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


n = int(input())
board = [[0]*n for _ in range(n)]
k = int(input())
for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    board[r-1][c-1] = 1
times = {}
l = int(input())
for _ in range(l):
    x, c = sys.stdin.readline().rstrip().split()
    times[int(x)] = c

# 상, 하, 좌, 우
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

direction = 1
time = 1
y, x = 0, 0 # 시작위치
snake = deque([[y, x]])
board[y][x] = 2 # 뱀위치 표현

while True:
    y, x = y + dy[direction], x+dx[direction]
    if 0 <= y < n and 0 <= x < n and board[y][x] != 2:
        if not board[y][x] == 1:
            delY, delX = snake.popleft()
            board[delY][delX] = 0
        board[y][x] = 2
        snake.append([y, x])
        if time in times.keys():
            direction = direction_chage(direction, times[time])
        time +=1

    else:
        break

print(time)