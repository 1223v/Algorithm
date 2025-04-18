def solution(n, money):


    dp = [0] * (n + 1)
    dp[0] = 1

    for i in money:
        for j in range(i,n+1):
            #print(dp[j - i],end='')
            dp[j] += dp[j - i]
        #print()


    #print(dp)
    return dp[n]%1000000007

print(solution(5,[1,2,5]))