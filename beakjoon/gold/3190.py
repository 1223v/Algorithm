import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
graph = [[0] * N for _ in range(N)]

di,dj = [1,0,-1,0],[0,-1,0,1]

for _ in range(K):
    i,j = map(int,input().split())
    graph[i-1][j-1] = 2

L = int(input())
move = []
for _ in range(L):
    move_time, direction = map(str,input().split())
    move.append((int(move_time), direction))


def bfs():

    queue = deque()
    visited = [[0] * N for _ in range(N)]

    queue.append((0,0))
    visited[0][0] = 1


    move_time, direction = move.pop(0)
    now_dir = 3

    while True:

        ci, cj = queue[-1]

        ni,nj = ci+di[now_dir], cj+dj[now_dir]

        if 0 <= ni < N and 0 <= nj < N and (ni,nj) not in queue:
            if graph[ni][nj] == 2:
                queue.append((ni,nj))
                visited[ni][nj] = visited[ci][cj] + 1
                graph[ni][nj] = 0


            elif graph[ni][nj] == 0:
                queue.append((ni,nj))
                queue.popleft()
                visited[ni][nj] = visited[ci][cj] + 1

        else:

            return visited[ci][cj]

        if move_time == visited[ci][cj]:
            if direction == 'L':
                now_dir = (now_dir-1) % 4
            else:
                now_dir = (now_dir + 1) % 4

            if len(move) > 0:
                move_time, direction = move.pop(0)


time = bfs()
print(time)
