import sys
input = sys.stdin.readline

s = list(map(int,input().rstrip()))
dp = [0] * (len(s)+1)



if s[0] == 0:
    print(0)
    exit()

s = [0] + s
dp[0] = 1
dp[1] = 1
for k in range(2,len(s)):

    if s[k] > 0:
        dp[k] += dp[k-1]

    if 10 <= s[k-1] * 10 + s[k] <= 26:
        dp[k] += dp[k-2]

print(dp[len(s)-1]%1000000)
