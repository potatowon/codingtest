'''
DFS 를 스택에 의해 설명하므로 Stack 으로 구현해 보자
'''


def dfs(graph, start_node):
    ## 이미 방문한 리스트와 방문이 필요한 리스트를 구현
    need, visited = [], []
    need.append(start_node)

    while need:
        node = need.pop()

        if node not in visited:
            visited.append(node)
            need.extend(graph[node])

    return visited

graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(dfs(graph, 'A'))