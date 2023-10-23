def dfs(graph, v, visited):
    visited[v] = True
    for j in range(len(graph[0])):
        if graph[v][j] == 1 and not visited[j]:
            dfs(graph, j, visited)

def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            dfs(computers, i, visited)
            answer += 1
    return answer
