import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = [i for i in range(1,n+1)]
s = [list(map(int,input().split())) for _ in range(m)]

for i in range(m):
    tmp = lst[s[i][0] - 1:s[i][1]]
    lst[s[i][0]-1:s[i][1]] = tmp[::-1]


print(*lst)