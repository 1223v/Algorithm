# 아기 상어 < 물고기 : 못지나감, 못먹음
# 아기 상어 > 물고기 : 지나감,먹음
# 아기 상어 = 물고기 : 지나감
# 먹을 수 있는 물고기가 1마리인 경우 그 물고기를 먹으러 감
# 더이상 물고기가 공간 안에 없다면 종료
# 먹을 수 있는 물고기가 1마리보다 많다면, 가장 가까운 물고기 탐색
# 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할때 지나는 최솟값
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기 그러한 물고기가 여러마리라면 가장 왼쪽에 있는 물고기를 먹는다
# 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력
# 물고기를 먹으면 그 칸은 빈칸이 됌
# 자신의 크기와 같은 수의 물고기를 먹을떄 마다 크기가 1 증가

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
s = [list(map(int,input().split())) for _ in range(N)]
di = [1,-1,0,0]
dj = [0,0,1,-1]

for i in range(N):
    for j in range(N):
        if s[i][j] == 9:
            ci,cj = i,j
            s[i][j] = 0

def bfs(si,sj):
    global shark

    queue = deque()
    visited = [[0] * N for _ in range(N)]

    queue.append((si,sj))
    visited[si][sj] = 1

    tlst = []
    distance = 0

    while queue:

        ci,cj = queue.popleft()

        if distance == visited[ci][cj]:
            return tlst,distance-1

        for i in range(4):
            ni,nj = ci+di[i], cj+dj[i]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and shark >= s[ni][nj]:
                queue.append((ni,nj))
                visited[ni][nj] = visited[ci][cj] + 1

                if shark > s[ni][nj]>0:
                    tlst.append((ni,nj))
                    distance = visited[ni][nj]

    return tlst, distance - 1





result = cnt = 0
shark = 2
while True:
    tlst, dist = bfs(ci,cj)
    if len(tlst) == 0:
        break

    tlst.sort(key=lambda x:(x[0],x[1]))
    ci,cj = tlst[0]
    cnt += 1
    result += dist
    s[ci][cj] = 0

    if shark == cnt:
        cnt = 0
        shark += 1

print(result)