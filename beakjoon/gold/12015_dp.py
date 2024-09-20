import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
dp = [0]

for i in s:
    if dp[-1] < i:
        dp.append(i)
    else:
        left = 0
        right = len(dp)

        while left < right:
            mid = (left + right) // 2
            if dp[mid] < i:
                left = mid + 1
            else:
                right = mid

        dp[right]=i
print(len(dp)-1)
