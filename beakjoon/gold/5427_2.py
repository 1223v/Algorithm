import sys
from collections import deque
input = sys.stdin.readline

TC = int(input())
di,dj = [0,0,1,-1],[1,-1,0,0]
for _ in range(TC):
    M,N = map(int,input().split())

    graph = [list(map(str,input().rstrip())) for _ in range(N)]
    s_queue = deque()
    f_queue = deque()
    f_visited = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if graph[i][j] == '@':
                s_queue.append((i,j))
                visited[i][j] = 1


            elif graph[i][j] == '*':
                f_queue.append((i,j))
                f_visited[i][j] = 1

    def bfs():

        while f_queue:
            ci, cj = f_queue.popleft()
            # print(ci,cj)
            for i in range(4):
                ni,nj = ci+ di[i], cj+dj[i]
                if 0 <= ni < N and 0 <= nj <M:
                    if f_visited[ni][nj] == 0 and graph[ni][nj] != '#':
                        f_visited[ni][nj] = f_visited[ci][cj] + 1
                        f_queue.append((ni,nj))


    def bfs1():
        while s_queue:
            ci, cj = s_queue.popleft()

            for i in range(4):
                ni, nj = ci + di[i], cj + dj[i]
                if ni >= N or nj >= M or ni < 0 or nj < 0:
                    return visited[ci][cj]
                if 0 <= ni < N and 0 <= nj < M:
                    if visited[ni][nj] == 0:
                        if (f_visited[ni][nj] == 0 or f_visited[ni][nj] > visited[ci][cj] + 1) and graph[ni][nj] == '.':
                            visited[ni][nj] = visited[ci][cj] + 1
                            s_queue.append((ni, nj))

        # for i in range(N):
        #     print(*visited[i])
        # print()
        # for i in range(N):
        #     print(*f_visited[i])
        return "IMPOSSIBLE"

    bfs()
    print(bfs1())




