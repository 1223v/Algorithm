import sys
input = sys.stdin.readline

N = int(input())

dp = [1] * N
s = []
for _ in range(N):
    s.append(int(input()))

for i in range(N):
    for j in range(i):
        if s[j] < s[i]:
            dp[i] = max(dp[i], dp[j]+1)


print(N-max(dp))