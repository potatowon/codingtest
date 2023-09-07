from collections import deque

def bfs(x, y, maps):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([(x, y)])
    count = int(maps[x][y])
    maps[x][y] = '0'  # 방문 표시

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] not in ['X', '0']:
                count += int(maps[nx][ny])
                maps[nx][ny] = '0'  # 방문 표시
                queue.append((nx, ny))
    
    return count

def solution(maps):
    islands = []
    maps = [list(row) for row in maps]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] not in ['X', '0']:
                islands.append(bfs(i, j, maps))
    
    if not islands:
        return [-1]
    
    return sorted(islands)

