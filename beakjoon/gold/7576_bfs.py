import sys
input = sys.stdin.readline
from collections import deque


N,M = map(int,input().split())
s = [list(map(int,input().split())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
tomato = []
di = [1,-1,0,0]
dj = [0,0,-1,1]
max_value= 0
def bfs():
    global max_value
    queue = deque()
    queue.extend(tomato)

    while queue:
        ci,cj,k = queue.popleft()
        max_value = max(k,max_value)
        for i in range(4):
            ni,nj = ci+di[i],cj+dj[i]
            if 0 <= ni < M and 0 <= nj < N:
                if s[ni][nj] == 0:
                    queue.append((ni,nj,k + 1))
                    s[ni][nj] = 1

    for i in s:
        if 0 in i:
            return -1

    return max_value


cnt = 0
nocnt = 0

for i in range(M):
    for j in range(N):
        if s[i][j] == 1:
            cnt += 1
            tomato.append((i,j,0))
        elif s[i][j] == 0:
            nocnt += 1



if cnt > 0 and nocnt > 0:
    print(bfs())

elif cnt > 0 and nocnt == 0:
    print(0)
else:
    print(-1)