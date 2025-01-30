import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

TC = int(input())

def dfs(v):
    global IsEven
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            check[i] = (check[v]+1) % 2
            dfs(i)

        elif check[v] == check[i]:
            IsEven = False

for _ in range(TC):
    N, E = map(int,input().split())
    IsEven = True
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    check = [0] * (N+1)


    for _ in range(E):
        s,e = map(int,input().split())
        graph[s].append(e)
        graph[e].append(s)

    for i in range(1,N+1):
        if IsEven:
            dfs(i)

        else:
            break

    if IsEven:
        print("YES")

    else:
        print("NO")
