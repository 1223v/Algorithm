import sys
input = sys.stdin.readline

n = int(input())
dp = [0,1]
mod = 1000000

p = mod // 10*15

for i in range(2, p):
    dp.append(dp[i-1] + dp[i-2])
    dp[i] %= mod

print(dp[n%p])