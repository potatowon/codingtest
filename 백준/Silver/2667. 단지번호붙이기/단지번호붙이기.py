import sys
from collections import deque, defaultdict
n = int(input())
aprt = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

m = [[0, 1], [0, -1], [-1, 0], [1, 0]]
counts = []  # 단지별 아파트 수를 저장하는 리스트
for rdx, row in enumerate(aprt):
    for cdx, col in enumerate(row):
        if (not visited[rdx][cdx]) and col == 1:
            x, y = rdx, cdx
            visited[x][y] = True
            q = deque([(x, y)])
            count = 1
            while q:
                x, y = q.popleft()
                for dx, dy in m:
                    if (x+dx >=0 and x+dx < n) and (y+dy>=0 and y+dy<n):
                        if (not visited[x+dx][y+dy]) and (aprt[x+dx][y+dy] ==1):
                            count += 1
                            q.append((x+dx, y+dy))
                            visited[x+dx][y+dy] = True
            counts.append(count)

print(len(counts))
counts.sort()
for i in counts:
    print(i)







