import sys
input = sys.stdin.readline

N = int(input())
s = list(map(int,input().split()))
reverse_s = s[::-1]
dp = [1] * N
reverse_dp = [1] * N

for i in range(N):
    for j in range(i):
        if s[j] < s[i]:
            dp[i] = max(dp[i], dp[j] + 1)
        if reverse_s[j] < reverse_s[i]:
            reverse_dp[i] = max(reverse_dp[i], reverse_dp[j]+1)

result = []
for i in range(N):
    result.append(dp[i] + reverse_dp[N-i-1] - 1)
print(max(result))
