import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N = int(input())
    dp = [0] * 100


    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2

    for i in range(4,N):
        dp[i] = dp[i-1] + dp[i-5]

    print(dp[N-1])