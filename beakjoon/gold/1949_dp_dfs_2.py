import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)
numbers = [0] + list(map(int,input().split()))
dp = [[0,0] for _ in range(N+1)]

for _ in range(N-1):
    u,v = map(int,input().split())
    A[u].append(v)
    A[v].append(u)

def dfs(v):
    visited[v] = True
    dp[v][1] += numbers[v]
    for i in A[v]:
        if not visited[i]:
            dfs(i)
            dp[v][0] += max(dp[i][0], dp[i][1]) # v 마을이 우수마을이 아닌 경우 i인 자식마을이 우수마을이 될 수 있고 아닐 수도 잇으니 자식망을 i에서 얻을 수 있는 최대 값을 선택하여 더한다
            dp[v][1] += dp[i][0] # v번째 마을이 우수마을인경우 자식마을 i는 우수마을이 될 수 없음 따라서 자식마을 i가 우수마을이 아닌 경우의 값을 더함


dfs(1)
print(max(dp[1]))
