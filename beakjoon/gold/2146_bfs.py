import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[-1]* (N) for _ in range(N)]
di = [0,0,1,-1]
dj = [1,-1,0,0]


def bfs(i,j, landmark):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = landmark


    while queue:
        ci,cj = queue.popleft()

        for i in range(4):
            ni,nj = ci + di[i], cj + dj[i]

            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == -1 and graph[ni][nj] == 1:
                    visited[ni][nj] = landmark

                    queue.append((ni,nj))



def bfs2(landmark):

    queue1 = deque()
    distance = [[-1] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == landmark:
                queue1.append((i,j))
                distance[i][j] = 0

    while queue1:
        ci,cj = queue1.popleft()

        for i in range(4):
            ni,nj = ci + di[i], cj + dj[i]
            if 0 <= ni < N and 0 <= nj < N:
                if graph[ni][nj] == 0 and visited[ni][nj] == -1 and distance[ni][nj] == -1:
                    queue1.append((ni,nj))

                    distance[ni][nj] = distance[ci][cj] + 1
                elif visited[ni][nj] != landmark and visited[ni][nj] != -1 and graph[ni][nj] == 1:

                    return distance[ci][cj]
    return float('inf')





landmark = 1
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == -1:
            bfs(i,j,landmark)
            landmark += 1

min_value = float('inf')
for i in range(1,landmark):
    min_value = min(min_value, bfs2(i))


print(min_value)
