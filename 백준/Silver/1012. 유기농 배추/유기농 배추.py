import sys
from collections import deque
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(i, j, visited, region):
    q = deque([[i, j]])
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < m) and (0 <= ny < n) and not visited[nx][ny] and region[nx][ny] == 1:
                visited[nx][ny] = True
                q.append([nx, ny])



t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split()) # 가로길이, 세로길이, 배추수
    region = [[0]*n for _ in range(m)]
    visited = [[False]*n for _ in range(m)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        region[x][y] = 1
    for rdx in range(m):
        for cdx in range(n):
            if region[rdx][cdx] == 1 and not visited[rdx][cdx]:
                bfs(rdx, cdx, visited, region)
                cnt += 1
    print(cnt)
