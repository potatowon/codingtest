from collections import deque
import copy


# 감염 전파
def bfs(temp_lab):
    global answer
    lr = [0, 0, -1, 1]  # 상, 하, 좌, 우
    ud = [1, -1, 0, 0]
    q = deque()

    # 초기 바이러스 위치를 찾아 큐에 삽입
    for row in range(n):
        for col in range(m):
            if temp_lab[row][col] == 2:
                q.append((row, col))

    while q:
        x, y = q.popleft()
        for dx, dy in zip(lr, ud):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and temp_lab[nx][ny] == 0:
                temp_lab[nx][ny] = 2
                q.append((nx, ny))

    cnt = sum(row.count(0) for row in temp_lab)
    answer = max(answer, cnt)


# 벽 세우기
def backTracking(wall_n, start_x, start_y):
    if wall_n == 3:
        temp_lab = copy.deepcopy(lab)  # lab 상태 저장
        bfs(temp_lab)  # BFS 실행
        return
    for row in range(start_x, n):
        for col in range(start_y if row == start_x else 0, m):
            if lab[row][col] == 0:
                lab[row][col] = 1
                backTracking(wall_n + 1, row, col)
                lab[row][col] = 0


n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

answer = 0
backTracking(0, 0, 0)
print(answer)
