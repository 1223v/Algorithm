### 주의. x, y | N, M 방향 신경쓸 것
import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
my_team = 0
enemy_team = 0
s = [input().rstrip() for _ in range(M)]
visited = [[False] * N for _ in range(M)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(n,color, x, y):
    global my_team, enemy_team
    queue = deque()
    queue.append((x,y))
    visited[y][x] = True
    n += 1

    while queue:
        (px, py) = queue.popleft()
        for i in range(4):
            nx,ny = px+dx[i], py+dy[i]

            if 0 <= nx < N and 0 <= ny < M:

                if not visited[ny][nx] and s[ny][nx] == color:
                    visited[ny][nx] = True
                    queue.append((nx,ny))
                    n += 1

    if color == "W":
        my_team += (n ** 2)
    else:
        enemy_team += (n**2)




for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            bfs(0,s[i][j], j,i)

print(my_team, enemy_team)