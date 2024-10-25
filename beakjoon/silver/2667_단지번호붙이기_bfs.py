import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
S = [list(map(str,input().rstrip())) for _ in range(N)]

di = [1,-1,0,0]
dj = [0,0,-1,1]

def bfs(n,i,j):
    queue = deque()
    queue.append((i,j))

    S[i][j] = "2"

    while queue:
        ci, cj = queue.popleft()
        n += 1
        for i in range(4):
            ni, nj = ci + di[i], cj + dj[i]
            if 0 <= ni < N and 0 <= nj < N:
                if S[ni][nj] == "1":
                    S[ni][nj] = "2"
                    queue.append((ni,nj))

    return n


result = []
for i in range(N):
    for j in range(N):
        if S[i][j] == "1":
            x = bfs(0,i,j)
            result.append(x)


result.sort()
print(len(result))
print('\n'.join(map(str, result)))