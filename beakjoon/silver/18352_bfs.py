import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

A = [[] for _ in range(N+1)]
visited = [-1] * (N+1)
result = []

def bfs(v):

    queue = deque()
    queue.append(v)
    visited[v] = 0

    while queue:
        x = queue.popleft()

        for i in A[x]:
            if visited[i] < 0:
                visited[i] = visited[x] + 1
                queue.append(i)




for _ in range(M):
    u,v = map(int, input().split())
    A[u].append(v)


bfs(X)

for i in range(N+1):
    if K == visited[i]:
        result.append(i)

if len(result) == 0:
    print(-1)

else:
    result.sort()
    for i in result:
        print(i)


