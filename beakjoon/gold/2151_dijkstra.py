#https://www.acmicpc.net/problem/2151

from collections import deque
import sys
input = sys.stdin.readline

di = [0,1,0,-1]
dj = [1,0,-1,0]

def bfs(si,sj):
    queue = deque()
    visited = [[[0] * 4 for _ in range(N)] for _ in range(N)]
    for dir in range(4):
        queue.append((si,sj,dir))
        visited[si][sj][dir] = 1

    while queue:
        ci,cj, cdir = queue.popleft()
        ni,nj = ci, cj
        while True:
            ni,nj = ni + di[cdir], nj + dj[cdir]
            if 0 <= nj < N and 0<= ni < N:



N = int(input())
bd = [list(input().rstrip()) for _ in range(N)]

si,sj = -1, -1
ei,ej = -1, -1

for i in range(N):
    for j in range(N):
        if bd[i][j] == '#':
            if si == -1:
                si,sj = i,j
                bd[si][sj] = 'S'
            else:
                ei,ej = i,j


print(bfs(si,sj))
