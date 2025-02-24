import sys
input = sys.stdin.readline

N = int(input())
s = list(map(int,input().split()))
dp = [float('inf')] * N

dp[0] = 0

for i in range(N):
    for j in range(i):
        if s[j] + j - i >= 0:
            dp[i] = min(dp[i],dp[j]+1)

if dp[N-1] < float('inf'):
    print(dp[N-1])
else:
    print(-1)