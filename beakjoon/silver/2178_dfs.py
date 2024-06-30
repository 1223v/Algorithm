import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N,M = map(int,input().split())
A = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

min_depth = float('inf')

for i in range(N):
    numbers = list(input())
    for j in range(M):
        A[i][j] = int(numbers[j])

def dfs(u,v,depth):
    global min_depth

    if u == N-1 and v == M-1:
        min_depth = min(depth, min_depth)
        return
    visited[u][v] = True
    for i in range(4):
        x = dx[i] + u
        y = dy[i] + v
        if x >= 0 and y >= 0 and x < N and y<M:
            if not visited[x][y] and A[x][y] == 1:
                dfs(x,y,depth+1)
    visited[u][v] = False # 백트래킹 : 모든 경우의 수를 탐색


dfs(0,0,1)
print(min_depth)
