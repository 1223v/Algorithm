import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)
# dp[v][0] : v가 얼리어답터가 아닌 경우의 최소 얼리어답터 수
# dp[v][1] : v가 얼리어답터인 경우 최소 얼리어답터 수
dp = [[0,0] for _ in range(N+1)]

for _ in range(N-1):
    u,v = map(int,input().split())
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
                # dp[v][1] : 노드 v가 얼리어답터인 경우
                # 자식 i는 얼리어답터 일수도 있고 아닐 수도 있음 -> min(dp[i][0],dp[i][1])을 더함
                dp[v][1] += min(dp[i][0], dp[i][1])
                # dp[v][0] : 노드 v가 얼리어답터가 아닌 경우
                # 자식 i는 반드시 얼리어답터가 되어야함. -> dp[i][1]을 더함
                dp[v][0] += dp[i][1]


dfs(1)
print(min(dp[1]))