import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int,input().split())
s = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

def bfs(v):
    global cnt
    queue = deque()
    queue.append(v)
    visited[v] = cnt

    while queue:
        x = queue.popleft()
        s[x].sort()
        for i in s[x]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                queue.append(i)


for _ in range(M):

    u,v = map(int,input().split())
    s[u].append(v)
    s[v].append(u)

bfs(R)

for i in range(1,N+1):
    print(visited[i])