import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

N,M = map(int,input().split())
answer = float('inf')
graph = [list(map(int,input().split())) for _ in range(N)]
virus = []
di = [0,0,1,-1]
dj = [1,-1,0,0]

def bfs(v):
    queue = deque(v)

    visited = [[-1] * N for _ in range(N)]
    m = 0


    for i,j in queue:
        visited[i][j] = 0

    while queue:
        ci,cj = queue.popleft()
        for i in range(4):
            ni,nj = ci + di[i], cj + dj[i]
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] == -1 and graph[ni][nj] != 1:
                    queue.append((ni,nj))
                    visited[ni][nj] = visited[ci][cj] + 1
                    m = max(visited[ni][nj], m)

    for i in range(N):
        for j in range(N):
            if graph[i][j] != 1 and visited[i][j] == -1:
                return float('inf')

    return m


for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus.append((i,j))

for v in combinations(virus,M):
    answer = min(bfs(v),answer)


if answer == float('inf'):
    print(-1)
else:
    print(answer)
