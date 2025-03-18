import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
di,dj = [0,0,1,-1], [1,-1,0,0]


for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            ci,cj = i,j
            graph[i][j] = 0


def bfs(i,j):
    queue = deque()
    visited = [[0] * N for _ in range(N)]

    queue.append((i,j))
    visited[i][j] = 1

    distance = 0
    tlst = []

    while queue:
        ci, cj = queue.popleft()

        if distance == visited[ci][cj]:
            return tlst,distance -1

        for i in range(4):
            ni,nj = ci + di[i],cj + dj[i]

            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == 0 and shark >= graph[ni][nj]:
                    queue.append((ni,nj))
                    visited[ni][nj] = visited[ci][cj] + 1

                    if shark > graph[ni][nj] >0:
                        tlst.append((ni,nj))
                        distance = visited[ni][nj]

    return tlst, distance-1

result = 0
levelup = 0
shark = 2

while True:

    tlst, distance = bfs(ci,cj)

    if len(tlst) == 0:
        break

    tlst.sort(key=lambda x:(x[0],x[1]))
    ci,cj = tlst[0]

    graph[ci][cj] = 0
    result += distance

    levelup += 1

    if shark == levelup:
        shark += 1
        levelup = 0




print(result)