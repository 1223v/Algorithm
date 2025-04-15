from collections import deque

di,dj = [0,0,1,-1],[1,-1,0,0]
def solution(maps):
    answer = 0
    N = len(maps)
    M = len(maps[0])
    visited = [[0] * M for _ in range(N)]

    def bfs(i,j):

        queue = deque()
        queue.append((i,j))
        visited[i][j] = 1

        while queue:
            ci,cj = queue.popleft()

            for x in range(4):
                ni,nj = ci + di[x], cj + dj[x]

                if 0 <= ni < N and 0 <= nj < M:
                    if visited[ni][nj] == 0 and maps[ni][nj] != 0:
                        visited[ni][nj] = visited[ci][cj] + 1
                        queue.append((ni,nj))

        # for i in range(N):
        #
        #     print(*visited[i])

    bfs(0,0)
    if visited[N-1][M-1] == 0:
        return -1
    else:
        return visited[N-1][M-1]




print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))