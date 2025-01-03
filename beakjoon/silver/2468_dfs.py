import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
max_value = 0

di = [1,-1,0,0]
dj = [0,0,1,-1]

def dfs(ci,cj,k):
    visited[ci][cj] = 1
    for i in range(4):
        ni,nj = ci + di[i], cj + dj[i]
        if 0 <= ni < N and 0 <= nj < N:
            if visited[ni][nj] == 0 and k < graph[ni][nj]:

                dfs(ni,nj,k)

    return 1


for k in range(0,100):
    visited = [[0] * N for _ in range(N)]
    tmp = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and visited[i][j] == 0:

                tmp += dfs(i,j,k)

    max_value = max(tmp,max_value)

print(max_value)