import sys
input = sys.stdin.readline

n = int(input())
s = [0] + list(map(int,input().split()))
dp = [0] * (n+1)
dp_num = []

for i in range(1, n+1):
    mx = 0
    for j in range(i):
        if s[i] > s[j]:
            mx = max(mx, dp[j])

    # print(s[dp.index(mx)])
    dp[i] = mx + 1

print(max(dp))

max_s = max(dp)
for i in range(n,0, -1):
    if dp[i] == max_s:

        dp_num.append(s[i])
        max_s -= 1

print(*dp_num[::-1])