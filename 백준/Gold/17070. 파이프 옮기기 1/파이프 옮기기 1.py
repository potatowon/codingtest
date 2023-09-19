import sys

def recursive(y, x, shape):
    global ans
    if y > n or x > n: # 벽보다 커지면 return 
        return 0
    if y == n and x == n: # n, n에 도달하게 되면 +1 
        return 1
    if dp[y][x][shape] != -1: # 이미 계산된 값이 있다면 그 값을 바로 반환
        return dp[y][x][shape]

    dp[y][x][shape] = 0
    # 0 -> 0 , 2 -> 0 이동 
    if home[y][x+1] == 0 and (shape == 0 or shape == 2):
        dp[y][x][shape] += recursive(y, x+1, 0)
    # 1 -> 1 , 2 -> 1 이동
    if home[y+1][x] == 0 and (shape == 1 or shape == 2):
        dp[y][x][shape] += recursive(y+1, x, 1)
    # 2 -> 2 이동
    if home[y+1][x] == 0 and home[y][x+1] == 0 and home[y+1][x+1] == 0:
        dp[y][x][shape] += recursive(y+1, x+1, 2)
    
    return dp[y][x][shape]

n = int(input())
home = [[0 for _ in range(n+2)] for _ in range(n+2)] # 만들어 지는 n,n 의 최대를 그림
for i in range(1, n+1):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(1, n+1):
        home[i][j] = row[j-1]

# -1로 초기화된 메모이제이션 배열 dp 선언
dp = [[[-1 for _ in range(3)] for _ in range(n+2)] for _ in range(n+2)]
        
print(recursive(1, 2, 0))
