import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N = int(input())

    dp = [[0,0] for _ in range(41)]

    dp[0][0], dp[0][1] = 1,0
    dp[1][0], dp[1][1] = 0,1

    for i in range(2,N+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]


    print(dp[N][0],dp[N][1])


