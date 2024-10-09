import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def bfs(si,sj):
    q = deque()
    visited2 = [[0]*5 for _ in range(5)]

    q.append((si,sj))
    visited2[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<5 and 0<=nj<5 and visited2[ni][nj] == 0 and visited1[ni][nj] ==1:
                q.append((ni, nj))
                visited2[ni][nj] =1
                cnt += 1
    return cnt==7


def check():
    for i in range(5):
        for j in range(5):
            if visited1[i][j] == 1:
                return bfs(i,j)
def dfs(n, cnt, scnt):
    global ans

    if cnt >7:
        return
    if n == 25:
        if cnt == 7 and scnt >=4:
            if check():
                ans += 1
        return

    visited1[n//5][n%5]=1
    dfs(n+1, cnt+1, scnt+int(arr[n//5][n%5]=='S'))
    visited1[n//5][n%5]=0
    dfs(n+1,cnt,scnt)


arr = [input() for _ in range(5)]
ans = 0
visited1 = [[0]*5 for _ in range(5)]
# 학생번호(0~24), 포함학생수, 다솜파 학생수
dfs(0, 0, 0)
print(ans)