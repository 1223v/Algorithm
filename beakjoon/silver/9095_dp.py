import sys
input = sys.stdin.readline

T = int(input())

# dp[4] = dp[3] + dp[2] + dp[1]
# 7개 = 4개 + 2개 + 1개

for _ in range(T):
    N = int(input())
    dp = [0] * (N+1)

    for i in range(1,N+1):
        # dp 테이블 갱신
        if i == 1: # 1인 경우의 수는 1개. dp 테이블에 저장
            dp[i] = 1
        elif i == 2: # 2인 경우의 수는 2개. dp테이블에 저장
            dp[i] = 2
        elif i == 3: # 3인 경우의 수는 4개. dp테이블에 저장
            dp[i] = 4
        else: # 위 조건이 아닌 경우부터는 점화식을 응용
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[N])