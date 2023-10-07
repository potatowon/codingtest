from collections import deque

def bfs(N, K):
    MAX_SIZE = 100001
    visited = [False] * MAX_SIZE
    queue = deque([(N, 0)])  
    
    while queue:
        curr_pos, curr_time = queue.popleft()
        
        if curr_pos == K:
            return curr_time
        
        if 0 <= curr_pos - 1 < MAX_SIZE and not visited[curr_pos - 1]:
            visited[curr_pos - 1] = True
            queue.append((curr_pos - 1, curr_time + 1))
        
        if 0 <= curr_pos + 1 < MAX_SIZE and not visited[curr_pos + 1]:
            visited[curr_pos + 1] = True
            queue.append((curr_pos + 1, curr_time + 1))
        
        if 0 <= curr_pos * 2 < MAX_SIZE and not visited[curr_pos * 2]:
            visited[curr_pos * 2] = True
            queue.append((curr_pos * 2, curr_time + 1))

N, K = map(int, input().split())

result = bfs(N, K)
print(result)
