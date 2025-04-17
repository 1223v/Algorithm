import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

M,N = map(int,input().split())

graph = [list(map(int,input().rstrip())) for _ in range(N)]
moves = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs():
    queue = deque()
    visited = [[float('inf')] * M for _ in range(N)]

    queue.append((0,0))
    visited[0][0] = 0

    while queue:
        ci,cj = queue.popleft()

        if (ci,cj) == (N-1,M-1):
            print(visited[N-1][M-1])
            # for i in range(N):
            #     print(*visited[i])
            exit()

        for di,dj in moves:
            ni,nj = ci + di, cj +dj

            if 0<= ni < N and 0 <= nj < M:
                if visited[ni][nj] > visited[ci][cj] + 1:


                    if graph[ni][nj] == 0:
                        visited[ni][nj] = visited[ci][cj]
                        queue.appendleft((ni, nj))

                    else:
                        visited[ni][nj] = visited[ci][cj] + 1
                        queue.append((ni, nj))


bfs()




