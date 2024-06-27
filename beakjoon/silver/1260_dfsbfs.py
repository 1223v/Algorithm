import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

N,M,S = map(int,input().split())
A = [[] for _ in range(N+1)]
visited1 = [False] * (N+1)
visited2 = [False] * (N+1)
dfs_list = []
bfs_list = []

for _ in range(M):
    u,v = map(int,input().split())
    A[u].append(v)
    A[v].append(u)

# 작은 노드 순 방문 조건 주의
for i in range(N+1):
    A[i].sort()

def dfs(v):
    visited1[v] = True
    dfs_list.append(v)

    for i in A[v]:
        if not visited1[i]:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited2[v] = True
    bfs_list.append(v)


    while queue:
        x = queue.popleft()
        for i in A[x]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True
                bfs_list.append(i)


dfs(S)
bfs(S)

print(*dfs_list)
print(*bfs_list)
