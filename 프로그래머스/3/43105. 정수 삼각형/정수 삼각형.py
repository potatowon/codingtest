def solution(tri):
    dp = [[0]*len(i) for i in tri]
    dp[0][0] = tri[0][0]

    for idx in range(1, len(tri)):
        for jdx in range(len(dp[idx])):

            if jdx == 0 :
                dp[idx][jdx] = dp[idx-1][jdx] + tri[idx][jdx]
            elif jdx == len(dp[idx]) - 1:
                dp[idx][jdx] = dp[idx-1][jdx-1] + tri[idx][jdx]
            else:
                dp[idx][jdx] = max(dp[idx-1][jdx-1]+tri[idx][jdx], dp[idx-1][jdx]+tri[idx][jdx])
    
    return max(dp[len(tri)-1])  