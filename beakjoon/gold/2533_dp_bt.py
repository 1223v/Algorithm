import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
dp = [[0,0] for _ in range(N+1)]

for _ in range(N-1):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(v):

    visited[v] = 1
    dp[v][1] += 1
    for i in graph[v]:
        if visited[i] ==0:
            dfs(i)
            dp[v][1] += min(dp[i][0],dp[i][1])
            dp[v][0] += dp[i][1]

dfs(1)
print(min(dp[1]))