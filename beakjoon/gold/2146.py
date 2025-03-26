import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

di,dj = [1,0,-1,0],[0,1,0,-1]

def bfs(i,j,cnt):

    queue = deque()

    graph[i][j] = cnt
    visited[i][j] = 1
    queue.append((i,j))

    while queue:
        ci,cj = queue.popleft()

        for i in range(4):
            ni,nj = ci + di[i], cj + dj[i]
            if 0 <= ni < N and 0 <= nj < N:
                if graph[ni][nj] == 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    graph[ni][nj] = cnt
                    queue.append((ni,nj))


def bfs2(cnt):
    queue = deque()
    distance = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == cnt:
                queue.append((i,j))
                distance[i][j] = 1


    while queue:
        ci,cj = queue.popleft()

        for i in range(4):
            ni,nj = ci + di[i], cj + dj[i]
            if 0 <= ni < N and 0 <= nj < N:
                if graph[ni][nj] != cnt and graph[ni][nj] != 0:
                    return distance[ci][cj] -1
                if graph[ni][nj] == 0 and distance[ni][nj] == 0:
                    queue.append((ni,nj))
                    distance[ni][nj] = distance[ci][cj] + 1

    return float('inf')

# 대륙 찾기
cnt = 2
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            bfs(i,j,cnt)
            cnt += 1

# for i in range(N):
#     print(*graph[i])
# print()

min_value = float('inf')
for i in range(2,cnt):
      min_value = min(min_value, bfs2(i))

print(min_value)
