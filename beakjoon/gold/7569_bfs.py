import sys
input = sys.stdin.readline
from collections import deque

N, M, H = map(int,input().split())

s = [[list(map(int,input().split())) for _ in range(M)] for _ in range(H)]

di = [-1, 1, 0, 0, 0, 0]
dj = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


queue = deque()

def bfs():
    while queue:
        cz,ci,cj = queue.popleft()
        for i in range(6):
            nz, ni, nj = cz + dz[i], ci + di[i], cj + dj[i]
            if 0<= nz < H and 0 <= ni < M and 0 <= nj < N:
                if s[nz][ni][nj] == 0:
                    s[nz][ni][nj] = s[cz][ci][cj] + 1
                    queue.append((nz,ni,nj))


for z in range(H):
    for i in range(M):
        for j in range(N):
            if s[z][i][j] == 1:
                queue.append((z,i,j))


bfs()
day = 0
for z in range(H):
    for i in range(M):
        for j in range(N):
            if s[z][i][j] == 0:
                print(-1)
                exit()
            day = max(day, s[z][i][j])

print(day-1)







