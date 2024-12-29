import sys
input = sys.stdin.readline

N = int(input())
num_lst = [list(map(int,input().split())) for _ in range(N)]
dp = [[] for _ in range(N)]

for i in range(N):
    dp[i] += [0] * (i+1)

dp[0][0] = num_lst[0][0]
for i in range(1,N):

    for j in range(i+1):
        if j-1>=0 and i-1 >=0:

            dp[i][j] = dp[i-1][j-1] + num_lst[i][j]

        if len(dp[i-1]) > j >= 0:
            dp[i][j] = max(dp[i][j],dp[i-1][j] + num_lst[i][j])



print(max(dp[N-1]))
