import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

TC = int(input())

def dfs(v):
    global IsEven
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            check[i] = 1-check[v]
            dfs(i)
        elif check[v] == check[i]:
            IsEven = False

for _ in range(TC):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    check = [0] * (V+1)
    IsEven = True
    for _ in range(E):
        s,e = map(int,input().split())
        graph[s].append(e)
        graph[e].append(s)

    for i in range(1,V+1):
        if IsEven:
            dfs(i)

        else:
            break

    if IsEven:
        print("YES")
    else:
        print("NO")