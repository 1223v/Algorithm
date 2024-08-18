import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
A = [[] for _ in range(n+1)]
answer = [0] * (n+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in A[x]:
            if not visited[i]:
                visited[i] = True
                answer[i] += 1
                queue.append(i)


for _ in range(m):
    u,v = map(int, input().split())
    A[u].append(v)

for i in range(1, n+1):
    visited = [False] * (n+1)
    BFS(i)

maxVal = 0
for i in range(1, n+1):
    maxVal = max(maxVal, answer[i])

for i in range(1,n+1):
    if maxVal == answer[i]:
        print(i, end=' ')


