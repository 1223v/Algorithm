import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)

N, M, R = map(int,input().split())

visited = [0] * (N+1)
cnt = 1
s = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    s[x].append(y)
    s[y].append(x)
def dfs(v):
    global cnt
    visited[v] = cnt
    s[v].sort()
    for j in s[v]:
        if not visited[j]:
            cnt += 1
            dfs(j)



dfs(R)

for i in range(1,N+1):
    print(visited[i])
