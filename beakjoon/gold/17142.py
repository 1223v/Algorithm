import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

di = [0,0,1,-1]
dj = [1,-1,0,0]

virus = []


for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus.append((i,j))


def bfs(v_lst):
    queue = deque(v_lst)
    visited = [[-1] * N for _ in range(N)]
    blanks = sum(row.count(0) for row in graph)  # 빈 칸 개수 저장

    for i, j in v_lst:
        visited[i][j] = 0

    time = 0
    while queue:

        if blanks == 0:
            return time  # 모든 빈 칸이 감염되었으면 즉시 반환

        time += 1
        for _ in range(len(queue)):  # 같은 초 동안 퍼질 바이러스만 실행
            ci, cj = queue.popleft()

            for i in range(4):
                ni, nj = ci + di[i], cj + dj[i]
                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == -1:
                    if graph[ni][nj] == 0:  # 빈 칸 감염
                        visited[ni][nj] = 1
                        blanks -= 1  # 빈 칸 개수 줄이기
                        queue.append((ni, nj))
                    elif graph[ni][nj] == 2:  # 비활성 바이러스 활성화
                        visited[ni][nj] = 1
                        queue.append((ni, nj))

    return float('inf')  # 모든 빈 칸이 감염되지 못한 경우



result = float('inf')
for i in combinations(virus,M):
    result = min(bfs(i), result)

if float('inf') == result:
    print(-1)
else:
    print(result)

