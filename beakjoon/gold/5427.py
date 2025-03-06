import sys
from collections import deque
input = sys.stdin.readline

TC = int(input())
di = [1,-1,0,0]
dj = [0,0,1,-1]

for _ in range(TC):
    M,N = map(int,input().split())

    graph = [list(map(str,input().rstrip())) for _ in range(N)]
    visited = [[-1] * (M) for _ in range(N)]
    fire_time = [[-1] * (M) for _ in range(N)]

    s_queue = deque()
    f_queue = deque()

    for i in range(N):
        for j in range(M):
            if graph[i][j] == '*':
                f_queue.append((i,j))
                fire_time[i][j] = 0

            elif graph[i][j] == '@':
                s_queue.append((i,j))
                visited[i][j] = 0

    while f_queue:
        ci,cj = f_queue.popleft()
        for i in range(4):
            ni,nj = ci + di[i], cj + dj[i]
            if 0 <= ni < N and 0 <= nj < M:
                if fire_time[ni][nj] == -1 and graph[ni][nj] == '.':
                    f_queue.append((ni, nj))
                    fire_time[ni][nj] = fire_time[ci][cj] + 1

    def bfs():
        while s_queue:
            ci, cj = s_queue.popleft()
            for i in range(4):
                ni, nj = ci + di[i], cj + dj[i]
                if not (0 <= ni < N and 0 <= nj < M):
                    return visited[ci][cj] + 1
                if graph[ni][nj] == '.' and visited[ni][nj] == -1:
                    if fire_time[ni][nj] == -1 or visited[ci][cj] + 1 < fire_time[ni][nj]:
                        s_queue.append((ni, nj))
                        visited[ni][nj] = visited[ci][cj] + 1

        return "IMPOSSIBLE"

    print(bfs())