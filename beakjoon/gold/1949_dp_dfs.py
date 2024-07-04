import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
# 각 노드드에 해당하는 값을 입력 받아 리스트로 저장 (1번 인덱스부터 시작)
numbers = [0] + list(map(int,input().split()))

A = [[] for _ in range(N+1)]
# dp 테이블 초기화
# dp[i][0] : 현재 I마을이 우수마을이 아닌경우
# dp[i][1] : 현재 I마을이 우수 마을인 경우

dp = [[0,0] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(N-1):
    u,v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)

def dfs(v):
    visited[v] = True
    dp[v][1] += numbers[v]
    for i in A[v]:
        if not visited[i]:
            dfs(i)
            dp[v][0] += max(dp[i][0],dp[i][1])
            dp[v][1] += dp[i][0]

dfs(1)
print(max(dp[1]))