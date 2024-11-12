# https://www.acmicpc.net/problem/4485

import sys
input = sys.stdin.readline
from collections import deque
di = [-1,1,0,0]
dj = [0,0,-1,1]
count = 1
while True:

    N = int(input())
    if N == 0:
        break

    else:

        s = [list(map(int,input().split())) for _ in range(N)]
        visited = [[sys.maxsize] * (N) for _ in range(N)]
        def bfs(i,j):
            queue = deque()
            queue.append((i,j))
            visited[i][j] = s[i][j]

            while queue:
                ci,cj = queue.popleft()

                for i in range(4):
                    ni,nj = ci+di[i], cj+dj[i]
                    if 0<= ni < N and 0 <= nj < N:

                        if visited[ni][nj] > visited[ci][cj] + s[ni][nj]:
                            visited[ni][nj] = visited[ci][cj] + s[ni][nj]
                            queue.append((ni, nj))






        bfs(0,0)
        print("Problem %d: %d" % (count, visited[N - 1][N - 1]))
        count += 1