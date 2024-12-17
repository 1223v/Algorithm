import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N,M = map(int,input().split())
s = [list(map(int,input().rstrip())) for _ in range(N)]
di = [1,-1,0,0]
dj = [0,0,1,-1]
def dfs(n,pi,pj):

    if pi == N-1 and s[pi][pj]==2:
        print("YES")
        exit()

    for i in range(4):
        ni,nj = pi + di[i], pj + dj[i]
        if 0 <= ni < N and 0 <= nj < M:
            if s[ni][nj] == 0:
                s[ni][nj] = 2
                dfs(n+1,ni,nj)


for j in range(M):
    if s[0][j] == 0:
        s[0][j] = 2
        dfs(0,0,j)


print("NO")
