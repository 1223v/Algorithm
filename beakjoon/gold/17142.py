import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

virus = []
blanks = 0  # 빈 칸 개수 저장

for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus.append((i, j))
        elif graph[i][j] == 0:
            blanks += 1  # 빈 칸 개수 카운트

def bfs(v_lst):
    queue = deque(v_lst)
    visited = [[-1] * N for _ in range(N)]


    for i, j in v_lst:
        visited[i][j] = 0

    max_time = 0
    while queue:

        ci, cj = queue.popleft()

        for i in range(4):
            ni, nj = ci + di[i], cj + dj[i]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == -1:
                if graph[ni][nj] == 0:  # 빈 칸 감염
                    visited[ni][nj] = visited[ci][cj] + 1
                    max_time = max(max_time, visited[ni][nj])  # 최장 시간 기록
                    queue.append((ni, nj))
                elif graph[ni][nj] == 2:  # 비활성 바이러스 활성화
                    visited[ni][nj] = visited[ci][cj] + 1
                    queue.append((ni, nj))

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0 and visited[i][j] == -1:
                return float('inf')

    return max_time

result = float('inf')
for i in combinations(virus, M):
    result = min(bfs(i), result)

if result == float('inf'):
    print(-1)
else:
    print(result)

