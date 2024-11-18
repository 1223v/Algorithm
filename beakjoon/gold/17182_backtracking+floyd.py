# https://www.acmicpc.net/problem/17182

import sys
input = sys.stdin.readline

N,K = map(int,input().split())
min_value = int(1e9)
s = [list(map(int,input().split())) for _ in range(N)]
visited = [False] * N
def dfs(n,past,cnt):
    global min_value
    if cnt > min_value:
        return

    if n == N:
        min_value = min(min_value, cnt)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(n+1, i, cnt + s[past][i])
            visited[i] = False

# 플로이드 와샬
for k in range(N):
    for i in range(N):
        for j in range(N):
            s[i][j] = min(s[i][j], s[i][k] + s[k][j])

visited[K] = True
dfs(1,K,0)

print(min_value)