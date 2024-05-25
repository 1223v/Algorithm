import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n,m,k = map(int, input().split())

graph = [[0] * m for _ in range(n)]
for _ in range(k):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1

visit = [[False] * m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

res = 0

def dfs(x,y):
    global cnt
    for i in range(4): # 방향 벡터 돌리면서 인접한 쓰레기를 찾기
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx <n and 0 <= ny < m:
            if graph[nx][ny] == 1 and not visit[nx][ny]: # 인접한 쓰레기 중 아직 방문처리가 되지 않은 쓰레기라면 방문처리 후 cnt+1
                visit[nx][ny] = True
                cnt += 1
                dfs(nx,ny) # 새로운 재귀 호출

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visit[i][j]: # 그래프 탐색중 방문하지 않은 위치의 쓰레기를 발견하면 dfs 시작
            cnt = 1
            visit[i][j] = True
            dfs(i,j)
            res = max(res,cnt) # 가장 큰 쓰레기 저장

print(res)
