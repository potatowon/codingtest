'''
최단거리를 확인하는데 사용된다. 

인접한 노드를 모두 큐에 넣는다
단, 이미 방문한 큐는 넣지 않는다
'''

## 방문기준 : 번호가 낮은 인접 노드 부터

from collections import deque

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True   # 현재노드 방문처리

    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


visited = [False] * 9
graph = [
    [],
    [2, 3, 8],
    [1,7 ],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7], 
    [2, 6, 8],
    [1, 7]
]

print(bfs(graph, 1, visited))