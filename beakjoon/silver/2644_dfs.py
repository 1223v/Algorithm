import sys
input = sys.stdin.readline

N = int(input())
target1, target2= map(int,input().split())
visited = [False] * (N+1)
s = [[] for _ in range(N+1)]
M = int(input())

for _ in range(M):
    u,v = map(int,input().split())
    s[u].append(v)
    s[v].append(u)

chk = False
def dfs(n, start, end):
    global chk
    visited[start] = True


    if start == end:
        print(n)
        chk = True
        exit()

    for i in s[start]:
        if not visited[i]:
            dfs(n+1, i, end)

dfs(0,target1, target2)

if not chk:
    print(-1)