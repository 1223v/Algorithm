import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
increase_dp = [1] * n
decrease_dp = [1] * n

for i in range(n):
    for j in range(i):
        if s[i] > s[j]:
            increase_dp[i] = max(increase_dp[i], increase_dp[j] +1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1 ):
        if s[i] > s[j]:
            decrease_dp[i] = max(decrease_dp[i], decrease_dp[j]+1)

result = [0] * n
for i in range(n):
    result[i] = increase_dp[i] + decrease_dp[i] -1

print(max(result))