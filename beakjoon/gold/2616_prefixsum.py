import sys
input = sys.stdin.readline

N = int(input())
graph = list(map(int,input().split()))
M = int(input())

S = [0] * (N+1)

for i in range(1,N+1):
    S[i] = S[i-1] + graph[i-1]


dp = [[0] * (N+1) for _ in range(4)]

for i in range(1,4):
    for j in range(i*M,N+1):
        if i == 1:
            dp[i][j] = max(dp[i][j-1], (S[j] - S[j-M]))

        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j-M] + S[j] - S[j-M])


# print(dp)
print(dp[3][N])
# print(S)