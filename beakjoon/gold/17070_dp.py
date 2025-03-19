import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

dp1 = [[0] * N for _ in range(N)]
dp2 = [[0] * N for _ in range(N)]
dp3 = [[0] * N for _ in range(N)]

dp1[0][1] = 1

for i in range(2,N):
    if graph[0][i] == 0:
        dp1[0][i] = dp1[0][i-1]

for i in range(1,N):
    for j in range(1,N):
        if graph[i][j] == 0 and graph[i][j-1] == 0 and graph[i-1][j] == 0:
            dp3[i][j] = dp1[i-1][j-1] + dp2[i-1][j-1] + dp3[i-1][j-1]

        if graph[i][j] == 0:
            dp2[i][j] = dp2[i-1][j] + dp3[i-1][j]
            dp1[i][j] = dp1[i][j-1] + dp3[i][j-1]

print(dp1[N-1][N-1] + dp2[N-1][N-1] + dp3[N-1][N-1])
print(dp1,dp2,dp3)