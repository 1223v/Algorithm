import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
A = [[] for _ in range(n+1)]
answer = [0] *(n+1)

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
                answer[v] += 1


for _ in range(m):
    u,v = map(int, input().split())
    A[v].append(u)

maxValue = 0
result = []
for i in range(1,n+1):
    visited = [False] * (n+1)
    bfs(i)
    if maxValue < answer[i]:
        maxValue = answer[i]
        result.clear()
        result.append(i)
    elif maxValue == answer[i]:
        result.append(i)

print(*result)

