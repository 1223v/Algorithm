import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N,M = map(int,input().split())

s= [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u,v = map(int,input().split())
    s[u].append(v)

F = int(input())
F_lst = list(map(int, input().split()))

chk = False
def dfs(v):
    global chk

    if v in F_lst:
        return

    if len(s[v]) == 0:
        chk = True
    else:
        for i in s[v]:
            if not visited[i]:
                visited[i] = True
                dfs(i)
                visited[i] = False


dfs(1)
if chk:
    print("yes")
else:
    print("Yes")




