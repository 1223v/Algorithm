import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N,M = map(int,input().split())
A = [[] for _ in range(N)]
visited = [False] * N
arrive = False
depth = 1

for _ in range(M):
    u,v = map(int,input().split())
    A[u].append(v)
    A[v].append(u)

def dfs(v):
    global depth,arrive
    if depth == 5:
        arrive = True
        return
    else:
        depth += 1
        visited[v] = True
        for i in A[v]:
            if not visited[i]:
                dfs(i)
        visited[v] = False
        depth -= 1

for i in range(N):
    dfs(i)
    depth =1
    if arrive:
        print(1)
        break

if not arrive:
    print(0)
