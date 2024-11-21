import sys

input = sys.stdin.readline

N, M = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(N)]

dp = [[-int(1e9)] * M for _ in range(N)]  # dp를 -1로 초기화
left = [[-int(1e9)] * M for _ in range(N)]
right = [[-int(1e9)] * M for _ in range(N)]

dp[0][0] = s[0][0]


for j in range(1,M):
    dp[0][j] = dp[0][j-1] + s[0][j]


for i in range(1,N):

    left[i][0] = dp[i-1][0] + s[i][0]
    for j in range(1,M):
        left[i][j] = max(dp[i-1][j] + s[i][j], left[i][j-1]+s[i][j])

    right[i][M-1] = dp[i-1][M-1] + s[i][M-1]
    for j in range(M-2,-1,-1):
        right[i][j] = max(dp[i-1][j] + s[i][j], right[i][j+1] + s[i][j])

    for j in range(M):
        dp[i][j] = max(right[i][j],left[i][j])


print(dp[N-1][M-1])

