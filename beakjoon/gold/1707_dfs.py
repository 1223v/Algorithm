import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(v):
    global IsEven
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            check[i] = (check[v]+1) % 2
            dfs(i)
        elif check[v] == check[i]:
            IsEven = False

N = int(input())
IsEven = True

for _ in range(N):
    u,v = map(int, input().split())
    A = [[] for _ in range(u+1)]
    visited = [False] * (u+1)
    check = [0] * (u+1)
    IsEven = True

    for i in range(v):
        s,e = map(int, input().split())
        A[s].append(e)
        A[e].append(s)

    for i in range(1, u+1):
        if IsEven:
            dfs(i)

        else:
            break

    if IsEven:
        print("YES")
    else:
        print("NO")
