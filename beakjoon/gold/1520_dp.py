import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n,m = map(int,input().split())

# 범위체크를 생략하기 위해서 0으로 둘러쌈
arr = [[0]*(m+2)] + [[0]+list(map(int, input().split())) + [0] for _ in range(n)] + [[0]*(m+2)]

# dp 테이블 생성 및 초기값 설정
dp = [[-1] * (m+2) for _ in range(n+2)]
dp[1][1] = 1 # 매우 중요

def dfs(ci, cj):
    if dp[ci][cj] == -1: # 첫방문
        # 네방향 (더 높은곳으로 부터 낮은곳 방문시 경로 수 누적
        dp[ci][cj] = 0
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            pi, pj = ci+di, cj+dj
            if arr[pi][pj] > arr[ci][cj]: #내리막길인 경우
                dp[ci][cj] += dfs(pi, pj) # 4방향 경로 수 누적

    return dp[ci][cj]

print(dfs(n,m))
