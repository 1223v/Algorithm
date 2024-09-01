import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

def dfs(n, cnt):
    global ans
    if ans >= (cnt+L-n): # 남은자리 다 놓아도 정답
        return
    if n == L:
        ans = max(ans, cnt)
        return

    for ci,cj in lst[n]: # 현재 사선번호에서 가능한 위치 하나씩 놓고 다음 사선으로
        if visited[ci-cj] == 0:
            visited[ci-cj] = 1
            dfs(n+1,cnt+1)
            visited[ci-cj] = 0
    dfs(n+1,cnt) # 이번 사선에서 안놓고 다음 사선으로 이동


lst = [[] for _ in range(2*N)]
visited = [0] * (2*N)
L = 2* N-1

for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            lst[i+j].append((i,j))


ans = 0
dfs(0,0)
print(ans)