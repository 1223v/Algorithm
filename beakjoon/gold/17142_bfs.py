import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

di = [0,0,1,-1]
dj = [1,-1,0,0]

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
queue = deque()

def bfs(v):
    global cnt
    visited = [[-1] * N for _ in range(N)]
    for i,j in v:
        queue.append((i,j))
        visited[i][j] = 0

    max_value = 0


    while queue:
        ci,cj = queue.popleft()

        for i in range(4):
            ni,nj = ci + di[i], cj + dj[i]

            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == -1 and graph[ni][nj] == 2:

                    visited[ni][nj] = visited[ci][cj] + 1
                    queue.append((ni,nj))

                elif visited[ni][nj] == -1 and graph[ni][nj] != 1:
                    max_value = max(max_value, visited[ci][cj] + 1)

                    visited[ni][nj] = visited[ci][cj] + 1
                    queue.append((ni,nj))



    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0 and visited[i][j] == -1:
                return float('inf')


    return max_value






virus = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus.append((i,j))


min_value = float('inf')
for i in combinations(virus,M):

    min_value = min(bfs(i),min_value)

if min_value != float('inf'):
    print(min_value)

else:
    print(-1)


