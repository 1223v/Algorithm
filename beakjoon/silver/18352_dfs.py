import sys
input = sys.stdin.readline
from collections import deque

N, M, K, X = map(int,input().split())
s = [[] for _ in range(N+1)]
visited = [-1] * (N+1)

for _ in range(M):
    u,v = map(int,input().split())
    s[u].append(v)

def dfs(n,v):

    if n > K:
        return

    for i in s[v]:
        if visited[i] != 0:
            visited[i] = min(visited[i], n)
        else:
            visited[i] = n
        dfs(n+1,i)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = 0

    while queue:
        x = queue.popleft()

        for i in s[x]:
            if visited[i] < 0:
                visited[i] = visited[x] + 1
                queue.append(i)
#dfs(1,X)
bfs(X)
chk = False
for i in range(1,N+1):
    if visited[i] == K:
        print(i)
        chk = True

if not chk:
    print(-1)