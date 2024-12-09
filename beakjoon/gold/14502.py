import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**5)


N,M = map(int,input().split())
s = [list(map(int,input().split())) for _ in range(N)]
result = 0
di = [1,-1,0,0]
dj = [0,0,1,-1]
def dfs(n):
    if n == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if s[i][j] == 0:
                s[i][j] = 1
                dfs(n+1)
                s[i][j] = 0

def bfs():
    global result

    tmp = [i[:] for i in s]
    queue = deque()
    ans = 0

    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                queue.append((i,j))

    while queue:
        pi, pj = queue.popleft()
        for i in range(4):
            ci,cj = pi + di[i], pj + dj[i]
            if 0 <= ci < N and 0 <= cj < M:
                if tmp[ci][cj] == 0:
                    tmp[ci][cj] = 2
                    queue.append((ci,cj))

    for i in tmp:
        ans += i.count(0)

    result = max(ans,result)


dfs(0)
print(result)