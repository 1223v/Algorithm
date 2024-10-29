import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

s = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
def bfs(i,j):
    queue = deque()
    queue.append(j)
    visited[i][j] = 1
    while queue:
        x = queue.popleft()
        for k in range(N):
            if s[x][k] == 1 and visited[i][k] != 1:
                queue.append(k)
                visited[i][k] = 1



for i in range(N):
    for j in range(N):
        if s[i][j]==1:
            bfs(i,j)

for i in visited:
    print(*i)