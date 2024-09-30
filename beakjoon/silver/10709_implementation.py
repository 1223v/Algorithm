import sys
input = sys.stdin.readline

n,m = map(int,input().split())
s = [input() for _ in range(n)]


for i in s:
    result = [-1 for _ in range(m)]
    for j in range(m):
        if i[j] == 'c':
            result[j] = 0

    tmp = 0
    for j in range(1,m):
        if result[j] == 0:
            tmp = 0
        if result[j-1] != -1 and result[j] != 0:
            tmp += 1
            result[j] = tmp
    print(*result)
