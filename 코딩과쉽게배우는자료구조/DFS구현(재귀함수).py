## DFS 깊이 우선 탐색
visited = [False] * 9 # index 0 제외 하기 위해 노드 최대값 + 1

def dfs(graph, v, visited):
    visited[v] = True       # 시작점 노트 방문처리
    print(v, end=' ')       # 방문한 노드 출력
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


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

dfs(graph, 1, visited)