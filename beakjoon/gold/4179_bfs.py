import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
di = [1,-1,0,0]
dj = [0,0,1,-1]
graph = [list(map(str, input().rstrip())) for _ in range(N)]
queue = deque()
visited = [[0] * M for _ in range(N)]

jihun = []
fire = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'J':
            jihun.append((i,j))
        elif graph[i][j] == 'F':
            fire.append((i, j))

queue.append((jihun[0][0],jihun[0][1],1))
visited[jihun[0][0]][jihun[0][1]] = 0


for i,j in fire:
    queue.append((i,j,0))
    graph[i][j] = '#'


while queue:
    ci,cj,k = queue.popleft()

    if ci == 0 or cj == 0 or ci == N-1 or cj == M-1:
        if k == 1 and graph[ci][cj] != '#':
            print(visited[ci][cj]+1)
            exit()

    for i in range(4):
        ni,nj = ci+di[i], cj + dj[i]
        if 0 <= ni < N and 0 <= nj < M:
            if graph[ni][nj] == '.' and k == 1 and graph[ci][cj] != '#':
                    visited[ni][nj] = visited[ci][cj] + 1
                    graph[ni][nj] = 'J'
                    queue.append((ni,nj,1))

            elif graph[ni][nj] != '#' and k == 0:
                visited[ni][nj] = float('inf')
                graph[ni][nj] = '#'
                queue.append((ni, nj, 0))


print("IMPOSSIBLE")