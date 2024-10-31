import sys
input = sys.stdin.readline

N = int(input())

start = 0
end = N
result = 0
while start <= end:
    mid = int((start + end) / 2)

    if mid * mid < N:
        start = mid + 1


    else:
        end = mid - 1
        result = mid

print(result)
