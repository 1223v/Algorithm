import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
di, dj = [0, 0, 1, -1], [1, -1, 0, 0]
graph = [list(map(int, input().split())) for _ in range(N)]

days = 0
def bfs(tlst):
    global days
    queue = deque(tlst)
    visited = [[0] * N for _ in range(N)]

    while queue:
        new_tree = []
        while queue:
            ci, cj = queue.popleft()

            cnt = 0
            for i in range(4):
                ni, nj = ci + di[i], cj + dj[i]

                if 0 <= ni < N and 0 <= nj < N:
                    if graph[ni][nj] == 0:
                        cnt += 1

            visited[ci][cj] = cnt

        for i in range(N):
            for j in range(N):
                if visited[i][j] !=0:
                    graph[i][j] -= visited[i][j]
                    if graph[i][j] < 0:
                        graph[i][j] = 0
                    visited[i][j] = 0
                if graph[i][j] != 0:
                    new_tree.append((i,j))

        # for i in range(N):
        #     print(*graph[i])
        # print(new_tree)
        days += 1
        queue.extend(new_tree)


tree = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            tree.append((i, j))

bfs(tree)
print(days)




