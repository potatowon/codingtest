from collections import deque
import sys

def moveKnight(start, chess, visited, end):
    x, y = start
    if start == end:
        return 0
    # print(x, y)
    visited[x][y] = True
    move = [[1, 2], [-1, 2], [1, -2], [-1, -2], [-2, 1], [-2, -1], [2, 1], [2, -1]]  # 수정된 부분
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for dx, dy in move:
            if (x + dx >= 0 and x+dx < len(chess)) and (y+dy >= 0 and y+dy < len(chess)):
                if not visited[x+dx][y+dy]:
                    chess[x+dx][y+dy] = chess[x][y] + 1
                    q.append((x+dx,y+dy))
                    visited[x+dx][y+dy] = True

    xx, yy = end

    return chess[xx][yy]

t = int(input())
for _ in range(t):
    l = int(input())
    chess = [[0]*l for _ in range(l)]
    visited = [[False]*l for _ in range(l)]
    start = tuple(map(int, sys.stdin.readline().split()))
    end = tuple(map(int, sys.stdin.readline().split()))
    # print(start, end)
    ans = moveKnight(start,chess, visited, end)

    print(ans)
