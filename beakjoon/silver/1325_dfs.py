import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
A = [[] for _ in range(n+1)]


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    cnt = 1
    while queue:
        x = queue.popleft()
        for i in A[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt += 1
    return cnt

for _ in range(m):
    u,v = map(int, input().split())
    A[v].append(u)

maxValue = 0
result = []
for i in range(1,n+1):
    visited = [False] * (n+1)
    cnts = bfs(i)
    if maxValue < cnts:
        maxValue = cnts
        result.clear()
        result.append(i)
    elif maxValue == cnts:
        result.append(i)

print(*result)
