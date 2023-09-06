from collections import deque
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = list(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)

for node in graph:
    node.sort()
# print(graph)
visited_1 = [False]*(n+1)
visited_2 = [False]*(n+1)

def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)

def bfs(graph, visited, v):
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        print(v , end= " ")
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
dfs(graph, visited_1, v)
print()
bfs(graph, visited_2, v)