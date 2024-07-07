import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)
dp = [[0,0] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int,input().split())
    A[u].append(v)
    A[v].append(u)

def dfs(v):
    visited[v] = True
    if len(A[v]) == 0:
        dp[v][1] = 1
        dp[v][0] = 0

    else:
        dp[v][1] += 1
        for i in A[v]:
            if not visited[i]:
                dfs(i)
                dp[v][1] += min(dp[i][0], dp[i][1])
                dp[v][0] += dp[i][1]

dfs(1)
print(min(dp[1]))