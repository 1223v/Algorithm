import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n,m = map(int,input().split())
visited = [False] * (n+1)
A = [[] for _ in range(n+1)]
arrive = False

def DFS(v, depth):
    global arrive

    if depth == 5:
        arrive = True
        return

    else:
        visited[v] = True
        for i in A[v]:
            if not visited[i]:
                DFS(i, depth+1)

    visited[v] = False

for _ in range(m):
    s,e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)


for i in range(n):
    DFS(i,1) # 시작 조건 유심히 파악할 것! => 깊이는 본인제외 다음 깊이부터 시작이니 0이 아닌 1
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)