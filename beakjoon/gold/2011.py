import sys
input = sys.stdin.readline

S = list(map(int,input().rstrip()))
dp = [0] * (len(S)+1)

if S[0] == 0:
    print(0)
    exit()

S = [0] + S
dp[0] = 1
dp[1] = 1

for i in range(2, len(S)):
    if S[i] > 0:
        dp[i] += dp[i-1]

    if 10 <= S[i-1] * 10 + S[i] <= 26:
        dp[i] += dp[i-2]

print(dp[-1] % 1000000)