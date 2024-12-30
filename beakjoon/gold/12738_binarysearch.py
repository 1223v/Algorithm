import sys
input = sys.stdin.readline

N = int(input())
s = list(map(int,input().split()))

dp = []
dp.append(s[0])
count = 0

for i in range(1,N):

    if dp[-1] < s[i]:
        dp.append(s[i])


    else:

        start = 0
        end = len(dp)-1
        while start < end:
            mid = (start + end) // 2

            if dp[mid] < s[i]:
                start = mid + 1

            else:
                end = mid

        dp[end] = s[i]


print(len(dp))

