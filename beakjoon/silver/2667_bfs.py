import sys
from collections import deque
input= sys.stdin.readline

N = int(input())
graph = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
di = [0,0,1,-1]
dj = [1,-1,0,0]

result = []

def bfs(ci,cj):
    queue = deque()
    cnt = 0

    queue.append((ci,cj))
    visited[ci][cj] = True

    while queue:
        pi,pj = queue.popleft()
        cnt += 1
        for i in range(4):
            ni,nj = pi+di[i], pj + dj[i]

            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj] and graph[ni][nj] == 1:
                    visited[ni][nj] = True
                    queue.append((ni,nj))

    result.append(cnt)

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 1:
            bfs(i,j)

result.sort()
print(len(result))
print(*result,sep="\n")
