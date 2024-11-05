import sys
input = sys.stdin.readline

N, M = map(int,input().split())

s = [[] for _ in range(N+1)]
visited = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    u,v = map(int,input().split())
    s[u].append(v)

def dfs(start,v):
    for i in s[v]:
        if not visited[start][i]:
            visited[start][i] = 1
            visited[i][start] = 1
            dfs(start,i)


for i in range(1,N+1):
    visited[i][i] = 1
    dfs(i,i)

answer = 0

for i in range(1,N+1):
    if sum(visited[i]) == N:
        answer += 1

print(answer)
