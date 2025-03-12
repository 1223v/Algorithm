import sys
input = sys.stdin.readline

N, M = map(int,input().split())
s = list(map(int,input().split()))

start = max(s)
end = sum(s)

while start <= end:
    mid = (start + end) // 2

    count,tmp = 1,0
    for i in range(N):
        if tmp + s[i] > mid:
            count += 1
            tmp = 0
        tmp += s[i]

    if count > M:
        start = mid + 1
    else:
        end = mid -1
print(start)
