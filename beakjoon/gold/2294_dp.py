import sys
input = sys.stdin.readline

N,K = map(int,input().split())
s = []
dp = [10001] * 10001
dp[0] = 0
for _ in range(N):
    s.append(int(input()))


for num in s:
    for i in range(num,K+1):
        dp[i] = min(dp[i],dp[i-num]+1)

if dp[K] == 10001:
    print(-1)
else:
    print(dp)
