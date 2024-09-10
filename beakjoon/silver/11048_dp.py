import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [[0]*(m+1)]+[[0]+list(map(int,input().split())) for _ in range(n)] # 패딩을 주어 (0,1), (1,0) 이런식으로 표를 생성
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = arr[i][j] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[n][m])
