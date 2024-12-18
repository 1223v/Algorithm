import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
di = [1,-1,0,0]
dj = [0,0,1,-1]

def bfs():
    queue = deque()
    queue.append((0,0,1))
    visited[0][0][1] = 1

    while queue:
        ci, cj, destroyed = queue.popleft()

        if ci == N-1 and cj == M-1:
            return visited[ci][cj][destroyed]

        for i in range(4):
            ni,nj = ci + di[i], cj + dj[i]
            if 0 <= ni < N and 0 <= nj < M:
                if graph[ni][nj] == 0 and visited[ni][nj][destroyed] == 0:
                    visited[ni][nj][destroyed] = visited[ci][cj][destroyed] + 1
                    queue.append((ni,nj,destroyed))

                if graph[ni][nj] == 1 and visited[ni][nj][0] == 0 and destroyed == 1:
                    visited[ni][nj][0] = visited[ci][cj][destroyed] + 1
                    queue.append((ni, nj, 0))

    return -1


print(bfs())