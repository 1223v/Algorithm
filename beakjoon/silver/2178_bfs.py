import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
A = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [1,-1,0,0] # 좌표 순서는 딱히 상관없는듯
dy = [0,0,1,-1]

for i in range(N):
    numbers = list(input())
    for j in range(M):
        A[i][j] = int(numbers[j])

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if x>= 0 and y >= 0 and x< N and y<M:
                if not visited[x][y] and A[x][y]:
                    visited[x][y] = True
                    A[x][y] = A[now[0]][now[1]] + 1
                    queue.append((x,y))

bfs(0,0)
print(A[N-1][M-1])