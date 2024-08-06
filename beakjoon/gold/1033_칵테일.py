import sys
input = sys.stdin.readline

N = int(input())
A = [[] for _ in range(N)]
visited = [False] * (N)
D = [0] * (N)
lcm = 1

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def dfs(v):
    visited[v] = True
    for i in A[v]:
        next = i[0]
        if not visited[next]:
            D[next] = D[v] * i[2] // i[1] # 다음 노드와 지금 노드의 비율
            dfs(next)


for i in range(N-1):
    a,b,p,q = map(int, input().split())
    A[a].append((b, p, q))
    A[b].append((a, q, p))
    lcm *= p * q // gcd(p,q)

D[0] = lcm
mgcd = D[0]
dfs(0)


for i in range(N):
    mgcd = gcd(mgcd, D[i])

for i in range(N):
    print((D[i]//mgcd), end=' ')