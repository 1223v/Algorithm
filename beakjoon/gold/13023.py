import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
A = [[] for _ in range(N)]
visited = [False] * N
arrive = False

for _ in range(M):
    u,v = map(int,input().split())
    A[u].append(v)
    A[v].append(u)

def dfs(v,depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    else:
        visited[v] = True
        for i in A[v]:
            if not visited[i]:
                dfs(i, depth+1)
        visited[v] = False

for i in range(N):
    dfs(i,1)
    if arrive:
        print(1)
        break

if not arrive:
    print(0)