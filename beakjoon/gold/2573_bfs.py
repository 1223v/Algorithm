import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
time = 0
di,dj = [0,0,1,-1], [1,-1,0,0]

def bfs(i,j):
    queue = deque()
    visited[i][j] = 1
    queue.append((i,j))

    while queue:
        ci,cj = queue.popleft()
        for i in range(4):
            ni,nj = ci + di[i], cj +dj[i]
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] == 0 and graph[ni][nj] > 0:
                    queue.append((ni,nj))
                    visited[ni][nj] = 1

                elif graph[ni][nj] == 0:
                    visited[ci][cj] += 1

while True:
    count = 0
    visited = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and graph[i][j] > 0:
                bfs(i,j)
                count += 1


    for i in range(N):
        for j in range(M):
            if visited[i][j] > 0:
                graph[i][j] -= (visited[i][j]-1)
                if graph[i][j] < 0:
                    graph[i][j] = 0


    if count > 1:
        print(time)
        break

    if count == 0:
        print(0)
        break

    time += 1