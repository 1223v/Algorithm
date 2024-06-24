import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int, input().split())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)

def bfs(v):

    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in A[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

for i in range(M):
    u,v = map(int,input().split())
    A[u].append(v)
    A[v].append(u)


count = 0

for i in range(1,N+1):
    if not visited[i]:
        count += 1
        bfs(i)

print(count)


