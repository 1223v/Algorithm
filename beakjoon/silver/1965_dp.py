import sys
input  = sys.stdin.readline

N = int(input())
s = list(map(int,input().split()))
dp = [0] * N
for i in range(N):
    for j in range(i):
        if s[j] < s[i]:
            dp[i] = max(dp[i], dp[j] + 1)



print(max(dp)+1)