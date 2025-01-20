import sys
from collections import deque
input = sys.stdin.readline

N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)


def dfs(v):
    visited[v] = True
    print(v,end=' ')
    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    visited[v] = True
    queue = deque()
    queue.append(v)

    while queue:
        x = queue.popleft()
        print(x,end=' ')
        graph[x].sort()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

dfs(V)
print()
visited = [False] * (N+1)
bfs(V)

