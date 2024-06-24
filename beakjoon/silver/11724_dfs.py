import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M = map(int,input().split())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)
def dfs(v):
    visited[v] = True

    for i in A[v]:
        if not visited[i]: # visited[i] 인점 유의 실수 주의
            dfs(i)

count = 0
for _ in range(M):
    u,v = map(int,input().split())
    A[u].append(v)
    A[v].append(u)

for i in range(1, N+1):
    if not visited[i]:

        dfs(i)
        count += 1


print(count)