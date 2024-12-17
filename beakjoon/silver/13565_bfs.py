import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
s = [list(map(int,input().rstrip())) for _ in range(N)]
di = [1,-1,0,0]
dj = [0,0,1,-1]
def bfs(pi,pj):
    queue = deque()
    queue.append((pi,pj))
    s[pi][pj] = 2
    while queue:
        ci,cj = queue.popleft()
        if ci == N-1 and s[ci][cj] == 2:
            print("YES")
            exit()
        for i in range(4):
            ni,nj = ci+di[i], cj+dj[i]
            if 0 <= ni < N and 0 <= nj < M:
                if s[ni][nj] == 0:
                    s[ni][nj] = 2
                    queue.append((ni,nj))

for j in range(M):
    if s[0][j] == 0:
        bfs(0,j)


print("NO")