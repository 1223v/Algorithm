import sys
input = sys.stdin.readline

n = int(input())
s = [int(input()) for _ in range(n)]

dp = [0] * (n) # dp 테이블 갱신

if len(s) <= 2:
    print(sum(s))

else:
    dp[0] = s[0] # 초기 dp값 설정
    dp[1] = s[0] + s[1] # 초기 dp 2번쨰 계단값 설정
    for i in range(2,n):
        dp[i] = max(dp[i-3]+s[i-1] + s[i], dp[i-2] + s[i]) # 2칸 올락는 경우와 한칸만 올라가는 경우 중 최대값 비교
    print(dp[n-1])