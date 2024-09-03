import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

#n == 1인 경우 dp[2]를 설정하면 index오류가 발생
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2] * 2



print(dp[n]%10007)