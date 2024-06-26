import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
A = [[] for _ in range(N)]
visited = [False] * N
arrive = False


for _ in range(M):
    u,v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)

def bfs(v):
    global arrive
    queue = deque([(v,1)])
    visited[v] = True

    while queue:
        x, depth = queue.popleft()

        if depth == 4:
            arrive = True
            break
        for i in A[x]:
            if not visited[i]:
                visited[i] = True
                queue.append((i,depth+1))
                visited[i] = False
        visited[v] =False



for i in range(N):
    bfs(i)
    if arrive:
        print(1)
        break

if not arrive:
    print(0)