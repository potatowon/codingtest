import sys
from collections import deque
t = int(input())
n = int(input())
graph = [[] for _ in range(t+1)]
visited = [False]*(t+1)
for _ in range(n):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)


def bfs(graph, i, visited):
    q = deque([i])
    visited[i] = True
    while q:
        # print(q)
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return visited
cnt = -1
vis = bfs(graph, 1, visited)
for i in vis[1:]:
    if i:
        cnt += 1
# print(vis)
print(cnt)