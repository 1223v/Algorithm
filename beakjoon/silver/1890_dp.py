import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

#dp 생성 및 초기값 설정
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] > 0 and arr[i][j] >0:
            jump = arr[i][j]
            # 오른쪽으로 이동
            if j + jump < n:
                dp[i][j+jump] += dp[i][j]
            # 아래로 이동
            if i + jump < n:
                dp[i+jump][j] += dp[i][j]

print(dp[n-1][n-1])