import sys
from collections import deque

input = sys.stdin.readline

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

TC = int(input())

for _ in range(TC):
    W, H = map(int, input().split())

    graph = [list(input().strip()) for _ in range(H)]
    fire_time = [[-1] * W for _ in range(H)]
    visited = [[-1] * W for _ in range(H)]

    fire_queue = deque()
    person_queue = deque()

    for i in range(H):
        for j in range(W):
            if graph[i][j] == '*':  # 불 위치
                fire_queue.append((i, j))
                fire_time[i][j] = 0
            elif graph[i][j] == '@':  # 상근이 위치
                person_queue.append((i, j))
                visited[i][j] = 0

    # 불의 BFS 수행
    while fire_queue:
        ci, cj = fire_queue.popleft()
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if 0 <= ni < H and 0 <= nj < W and graph[ni][nj] == '.' and fire_time[ni][nj] == -1:
                fire_time[ni][nj] = fire_time[ci][cj] + 1
                fire_queue.append((ni, nj))


    # 상근이의 BFS 수행
    def bfs():
        while person_queue:
            ci, cj = person_queue.popleft()
            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]
                if not (0 <= ni < H and 0 <= nj < W):  # 탈출 성공
                    return visited[ci][cj] + 1
                if graph[ni][nj] == '.' and visited[ni][nj] == -1:
                    if fire_time[ni][nj] == -1 or visited[ci][cj] + 1 < fire_time[ni][nj]:
                        visited[ni][nj] = visited[ci][cj] + 1
                        person_queue.append((ni, nj))
                        
        return "IMPOSSIBLE"


    print(bfs())