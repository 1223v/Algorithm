import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
s = [list(input().rstrip()) for _ in range(N)]

dx = [-1, 1,0,0]
dy = [0,0,1,-1]

open_x, open_y = -1, -1
close_x, close_y = -1, -1

for i in range(N):
    for j in range(N):
        if s[i][j] == '#':
            if open_x == -1 and open_y == -1:
                open_x, open_y = i,j
            else:
                close_x, close_y=i,j


check = [[[-1] * 4 for _ in range(N)] for _ in range(N)]
queue = deque()

for a in range(4):
    queue.append((open_x, open_y, a))
    check[open_x][open_y][a] = 0


while queue:
    x,y,dir = queue.popleft()

    if x == close_x and y == close_y:
        print(check[x][y][dir])
        break

    nx, ny = x + dx[dir], y + dy[dir]
    if 0 <= nx < N and 0 <= ny < N:
        if s[nx][ny] != '*':
            if check[nx][ny][dir] == -1 or check[nx][ny][dir] > check[x][y][dir]:
                check[nx][ny][dir] = check[x][y][dir]
                queue.appendleft((nx, ny,dir))


            if s[nx][ny] == '!':
                if dir < 2:
                    for n_dir in range(2,4):
                        if check[nx][ny][n_dir] == -1 or check[nx][ny][n_dir] > check[x][y][dir]+1:
                            check[nx][ny][n_dir] = check[x][y][dir] + 1
                            queue.append((nx,ny,n_dir))

                else:
                    for n_dir in range(2):
                        if check[nx][ny][n_dir] == -1 or check[nx][ny][n_dir] > check[x][y][dir]+1:
                            check[nx][ny][n_dir] = check[x][y][dir]+1
                            queue.append((nx,ny,n_dir))
