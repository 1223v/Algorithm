import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

N,M,R = map(int,input().split())
visited = [0] * (N+1)
s = [[] for _ in range(N+1)]
cnt = 1

for _ in range(M):
    v, w = map(int,input().split())
    s[v].append(w)
    s[w].append(v)

def dfs(v):
    global cnt
    visited[v] = cnt
    s[v].sort(reverse=True)
    for i in s[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

dfs(R)

for i in range(1,N+1):
    print(visited[i])
