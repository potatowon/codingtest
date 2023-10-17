from collections import deque

n = int(input())
region = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, visited, h):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and region[nx][ny] > h:
                visited[nx][ny] = True
                queue.append((nx, ny))

answer = 1  # 비가 오지 않는 경우를 대비하여 초기값을 1로 설정

for h in range(max(map(max, region))):  # 가장 높은 지역의 높이까지 반복
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if region[i][j] > h and not visited[i][j]:  # 해당 지역의 높이가 비의 높이보다 크고, 아직 방문하지 않았다면
                bfs(i, j, visited, h)
                cnt += 1
    answer = max(answer, cnt)

print(answer)
