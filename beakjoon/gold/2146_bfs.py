import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]

di,dj = [0,0,-1,1], [1,-1,0,0]

def bfs(i,j,count):
    queue = deque()

    visited[i][j] = 1
    graph[i][j] = count
    queue.append((i,j))

    while queue:
        ci,cj = queue.popleft()

        for i in range(4):
            ni,nj = ci + di[i], cj + dj[i]

            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == -1 and graph[ni][nj] == 1:
                    graph[ni][nj] = count
                    visited[ni][nj] = 1
                    queue.append((ni,nj))


def bfs2(count):
    queue1 = deque()
    distance = [[-1] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == count:
                queue1.append((i,j))
                distance[i][j] = 0

    while queue1:
        ci,cj = queue1.popleft()

        for i in range(4):
            ni,nj = ci + di[i], cj + dj[i]
            if 0 <= ni < N and 0 <= nj < N:
                if graph[ni][nj] != count and graph[ni][nj] != 0:
                    return distance[ci][cj]

                elif graph[ni][nj] == 0 and distance[ni][nj] == -1:
                    distance[ni][nj] = distance[ci][cj] + 1
                    queue1.append((ni,nj))
    return float('inf')





count = 1
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == -1:

            bfs(i,j,count)
            count += 1

min_value = float('inf')
for i in range(1,count):
    min_value = min(min_value,bfs2(i))

print(min_value)

