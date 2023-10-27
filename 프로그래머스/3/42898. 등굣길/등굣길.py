def solution(m, n, puddles):
    # 초기화
    dp = [[0]*m for _ in range(n)]
    
    for x, y in puddles:
        dp[y-1][x-1] = -1

    dp[0][0] = 1

    # 동적 프로그래밍
    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:
                continue
            if i - 1 >= 0 and dp[i-1][j] != -1:
                dp[i][j] += dp[i-1][j]
            if j - 1 >= 0 and dp[i][j-1] != -1:
                dp[i][j] += dp[i][j-1]

    return dp[n-1][m-1]%1000000007
