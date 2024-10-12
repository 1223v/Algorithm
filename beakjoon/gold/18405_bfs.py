import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int,input().split())
v_lst = [list(map(int,input().split())) for _ in range(N)]
v_point = []
S, X, Y = map(int,input().split())
X,Y = X-1, Y-1
visited = [[False] * N for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

result =0

def bfs(v,S):
    queue = deque(v)

    while queue:
        x,y,z = queue.popleft()
        if z == S:
            break

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                # 전염이 아직인 경우
                if v_lst[nx][ny] == 0:
                    v_lst[nx][ny] = v_lst[x][y]
                    queue.append((nx,ny,z+1))





for p in range(1,K+1):
    for i in range(N):
        for j in range(N):
            if p == v_lst[i][j]:
                v_point.append((i,j,0))


bfs(v_point,S)
print(v_lst[X][Y])