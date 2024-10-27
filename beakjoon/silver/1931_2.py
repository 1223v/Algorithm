import sys
input = sys.stdin.readline

N = int(input())
time_lst = []
for _ in range(N):
    s, e = map(int,input().split())
    time_lst.append((e,s))

time_lst.sort()
end = -1
result = 0
for i in range(N):
    if time_lst[i][1] >= end:
        end = time_lst[i][0]

        result += 1

print(result)