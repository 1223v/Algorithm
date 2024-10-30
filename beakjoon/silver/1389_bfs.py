import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
s = [[] for _ in range(N+1)]
min_value = sys.maxsize
visited = [False] * (N+1)
result = [sys.maxsize]
for _ in range(M):
    x, y = map(int,input().split())
    s[x].append(y)
    s[y].append(x)

def bfs(v,n):
    queue = deque()
    queue.append((v,n))
    visited[v] = True

    while queue:
        x,k = queue.popleft()
        for i in s[x]:
            if not visited[i]:
                visited[i] = True
                n += k+1
                queue.append((i,k+1))


    return n


for i in range(1,N+1):
    visited = [False] * (N+1)
    result.append(bfs(i,0))

print(result.index(min(result)))