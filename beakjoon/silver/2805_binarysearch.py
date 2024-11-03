import sys
input = sys.stdin.readline

N,M = map(int, input().split())
s = list(map(int,input().split()))

height = 0
start = 1
end = max(s)

while start <= end:
    mid = int((start + end)/2)
    result = 0
    for i in range(N):
        if s[i] - mid > 0:
            result += s[i] - mid
    if result >= M:
        start = mid + 1
        height = mid
    else:
        end = mid - 1



print(end)