import sys
input = sys.stdin.readline

N = int(input())
s = list(map(int,input().split()))
target = int(input())

start = 1
end = max(s)
result = 0
while start <= end:
    mid = int((start + end) / 2)
    total = 0
    for i in s:
        if i > mid:
            total += mid
        else:
            total += i

    if total <= target:
        start = mid+1
        result = mid

    elif total > target:
        end = mid-1

print(result)

