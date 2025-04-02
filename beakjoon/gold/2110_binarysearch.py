import sys
input = sys.stdin.readline

N,M = map(int,input().split())

S = sorted([int(input()) for _ in range(N)])

start = 1
end = S[-1] - S[0]
min_value = 0
while start <= end:

    mid = (start + end) // 2
    sum_value = S[0]
    count = 1


    for i in range(1,N):
        if S[i] >= sum_value + mid:
            sum_value = S[i]
            count += 1



    if count >= M:
        min_value = mid
        start = mid +1

    else:
        end = mid - 1

print(min_value)