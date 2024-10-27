import sys
input = sys.stdin.readline

N = int(input())
RGB_lst = []
dp = [[0]*3 for _ in range(N)]
for _ in range(N):
    r,g,b = map(int,input().split())
    RGB_lst.append((r,g,b))

dp[0][0] = RGB_lst[0][0]
dp[0][1] = RGB_lst[0][1]
dp[0][2] = RGB_lst[0][2]


for i in range(1,N):
    dp[i][0] = min(RGB_lst[i][0] + dp[i-1][1], RGB_lst[i][0] + dp[i-1][2])
    dp[i][1] = min(RGB_lst[i][1] + dp[i - 1][0], RGB_lst[i][1] + dp[i - 1][2])
    dp[i][2] = min(RGB_lst[i][2] + dp[i - 1][0], RGB_lst[i][2] + dp[i - 1][1])

print(min(dp[N-1]))
