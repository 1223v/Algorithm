import sys
from collections import deque
import copy
input = sys.stdin.readline

N,M = map(int,input().split())
s = [list(map(int,input().split())) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
result = 0

# 0은 빈칸, 1은 벽, 2는 바이러스
# 상하좌우로 퍼짐

# 바이러스 전파 bfs
def bfs():
    global result
    queue = deque()
    tmp = copy.deepcopy(s)
    ans = 0

    # 바이러스 찾기
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                queue.append((i,j))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = 2
                    queue.append((nx, ny))

    for i in tmp:
        ans += i.count(0)

    return ans

def dfs(cnt, lst):
    global result
    # 종료 조건 : 벽 3개 다 세움
    if cnt == 3:
        result = max(result, bfs())
        return

    for i,j in lst:
        if s[i][j] == 0:
            s[i][j] = 1
            dfs(cnt+1, lst)





dfs(0)
print(result)

lst = []
virus = []

for i in range(N):
    for j in range(M):
        if s[i][j] == 0:
            lst.append((i,j))
        elif s[i][j] == 2:
            virus.append((i,j))



