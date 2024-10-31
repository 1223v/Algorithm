import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

N, M, R = map(int,input().split())

s = [[] for _ in range(N+1)]
visited = [0] * (N+1)


for _ in range(M):
    u,v = map(int,input().split())
    s[u].append(v)
    s[v].append(u)


def dfs(n,v):

    visited[v] = n
    s[v].sort()
    for i in s[v]:
        if visited[i] == 0 and i != R:
            dfs(n+1,i)



dfs(0,R)

for i in range(1,N+1):
    if visited[i] != 0 or i == R:
        print(visited[i])
    else:
        print(-1)