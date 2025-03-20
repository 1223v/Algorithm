import sys
from collections import deque
input = sys.stdin.readline
from copy import deepcopy

N, M, T = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]
di,dj = [0,0,1,-1],[1,-1,0,0]

c_di,c_dj = [0,1,0,-1],[1,0,-1,0]

def dirty(graph):

    d_queue = deque()

    visited = [[0] * M for _ in range(N)]


    for i,j in dirty_pos:
        d_queue.append((i,j))


    while d_queue:

        ci,cj = d_queue.popleft()
        cnt = 0
        origin_dirty = graph[ci][cj]


        for i in range(4):
            ni,nj = ci + di[i], cj + dj[i]
            if 0 <= ni < N and 0 <= nj < M:
                if graph[ni][nj] != -1:
                    visited[ni][nj] += origin_dirty // 5


                    cnt += 1
        visited[ci][cj] += origin_dirty - origin_dirty//5 * cnt

    visited[cleaner[0][0]][cleaner[0][1]] = -1
    visited[cleaner[1][0]][cleaner[1][1]] = -1
    return visited


def clean_air():


    dr1 = 3
    ci1,cj1= cleaner[0]
    ni,nj = ci1-1,cj1

    while True:

        if ci1 == ni and cj1 == nj:
            break
        ci,cj = ni,nj
        ni,nj = ni + c_di[dr1], nj +c_dj[dr1]

        if not(0 <= ni < N and 0<= nj < M) or (ci1+1 == ni and dr1 == 1):
            dr1 = (dr1 + 1) % 4
            ni, nj = ci, cj

            continue
        if graph[ni][nj] == -1:
            graph[ci][cj] = 0
        else:
            graph[ci][cj] = graph[ni][nj]


    dr2 = 1
    ci2, cj2 = cleaner[1]
    ni, nj = ci2 + 1, cj2
    while True:
        if ci2 == ni and cj2 == nj:
            break
        ci, cj = ni, nj
        ni, nj = ni + c_di[dr2], nj + c_dj[dr2]

        if not (0 <= ni < N and 0 <= nj < M) or (ci2-1 == ni and dr2 == 3):
            dr2 = (dr2 - 1) % 4
            ni, nj = ci, cj
            continue
        if graph[ni][nj] == -1:
            graph[ci][cj] = 0
        else:
            graph[ci][cj] = graph[ni][nj]




for _ in range(T):

    cleaner = []
    dirty_pos = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == -1:
                cleaner.append((i, j))

            elif graph[i][j] > 0:

                dirty_pos.append((i, j))

    graph = dirty(graph)
    clean_air()

result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] > 0:
            result += graph[i][j]

print(result)