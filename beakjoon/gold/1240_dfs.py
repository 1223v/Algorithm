import sys
input = sys.stdin.readline

N,M = map(int,input().split())

s = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = 0

def dfs(n,v, end):
    global result

    visited[v] = True
    if end == v:
        result = n
        return


    elif result == 0:
        for i,value in s[v]:
            if not visited[i]:
                dfs(n+value,i,end)

for _ in range(N-1):
    start,end,v = map(int, input().split())

    s[start].append((end,v))
    s[end].append((start,v))


for _ in range(M):
    x,y = map(int,input().split())
    visited = [False] * (N + 1)
    result = 0
    dfs(0,x,y)
    print(result)