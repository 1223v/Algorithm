import sys
input = sys.stdin.readline

n = int(input())
s = [0] + list(map(int, input().split()))
dp = [0] * (n+1)

dp[0] = 0
for i in range(1,n+1):
    mx = 0
    for j in range(i):
        if s[j] < s[i]:
            mx = max(dp[j],mx)

    dp[i] = mx + s[i]

print(max(dp))