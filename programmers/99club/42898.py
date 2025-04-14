def solution(m, n, puddles):
    puddles = set(tuple(p) for p in puddles)
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1

    for j in range(1, m):
        if (j+1,1) not in puddles:
            dp[0][j] = dp[0][j-1]

    for i in range(1, n):
        if (1,i+1) not in puddles:
            dp[i][0] = dp[i-1][0]

    for i in range(1, n):
        for j in range(1, m):
            if (j+1,i+1) not in puddles:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007

    return dp[n-1][m-1] % 1000000007

print(solution(4, 3, [[2, 2]]))
