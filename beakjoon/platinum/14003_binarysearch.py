import sys
input = sys.stdin.readline


N = int(input())
s = list(map(int,input().split()))

lis = [[0,0] for _ in range(N)]
dp=[]

dp.append(s[0])
lis[0][0],lis[0][1] = 0, s[0]
result = []

for i in range(1,N):

    lis[i][1] = s[i]

    if dp[-1] < s[i]:
        lis[i][0] = len(dp)
        dp.append(s[i])

    else:
        start = 0
        end = len(dp)-1

        while start < end:
            mid = (start+end) // 2


            if dp[mid] < s[i]:
                start = mid + 1
            else:
                end = mid

        lis[i][0] = end
        dp[end] = s[i]

print(len(dp))

length = len(dp)-1
for i in range(len(lis)-1,-1,-1):
    if lis[i][0] == length:
        result.append(lis[i][1])
        length -= 1
    if length == -1:
        break


print(*result[::-1])
