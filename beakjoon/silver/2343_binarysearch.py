import sys
input = sys.stdin.readline

N, M = map(int,input().split())
S = list(map(int,input().split()))

start = max(S)
end = sum(S)

while start <= end:
    ssum = 0
    count = 1
    middle = int((start + end) / 2)
    for i in range(N):
        if ssum + S[i] > middle:
            count += 1
            ssum = 0
        ssum += S[i]

    if count > M:
        start = middle +1
    else:
        end = middle - 1

print(start)