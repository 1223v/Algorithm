import sys
input = sys.stdin.readline

N,M = map(int,input().split())
s = [0] * (N+1)
lst = [0] + list(map(int, input().split()))
count = 0

s[1] = lst[1]
for i in range(2,N+1):
    s[i] = s[i-1] + lst[i]

start = 1
end = 1
while start <= N and end <= N:

    if s[end] - s[start - 1] < M:
        end += 1

    elif s[end] - s[start - 1] > M:
        start += 1
    else:
        end+=1
        count += 1


# for i in range(1,N+1):
#     for j in range(i,N+1):
#         if s[j] - s[i-1] == M:
#             count += 1

print(count)
