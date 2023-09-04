import sys
from collections import deque
n, m = map(int, input().split()) # nxm
maze = [[0]*(m+2) for _ in range(n+2)]
for i in range(1, n+1):
    numbers = sys.stdin.readline().rstrip()
    for j, num in enumerate(numbers):
        maze[i][j+1] = int(num)

# print(maze)

visited = [[False]*(m+2) for _ in range(n+2)]

def bfs(maze, visited):
    x, y = 1, 1
    visited[x][y] = True
    lr = [0, 0, -1, 1] # 상, 하, 좌, 우
    ud = [1, -1, 0, 0]
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()

        for dx, dy in zip(lr, ud):
            if not visited[x + dx][y + dy]:
                if maze[x+dx][y+dy] == 1:
                    maze[x+dx][y+dy] = maze[x][y] + 1
                    # print(maze[x+dx][y+dy])
                    q.append((x+dx, y+dy))
                    visited[x+dx][y+dy] = True
    print(maze[n][m])


bfs(maze,visited)

