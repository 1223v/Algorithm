from collections import deque
di,dj = [0,0,1,-1],[1,-1,0,0]

def solution(board):
    answer = 0

    N = len(board)
    M = len(board[0])


    visited = [[float('inf')] * M for _ in range(N)]

    def bfs(start):

        queue = deque()
        queue.append(start)
        visited[start[0]][start[1]] = 0

        while queue:

            ci,cj = queue.popleft()

            if board[ci][cj] == 'G':
                return visited[ci][cj]

            for dr in range(4):
                ni,nj = ci,cj

                while True:
                    next_ni,next_nj = ni + di[dr], nj + dj[dr]


                    if not(0 <= next_ni < N and 0 <= next_nj < M) or board[next_ni][next_nj] == 'D':
                        break

                    ni,nj = next_ni, next_nj

                if (ni,nj) == (ci,cj):
                    continue

                if visited[ni][nj] > visited[ci][cj] + 1:
                    visited[ni][nj] = visited[ci][cj] + 1
                    queue.append((ni,nj))



        return -1



    R_info = (0,0)
    chk = False
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                R_info = (i,j)
                chk = True
                break
        if chk:
            break





    return bfs(R_info)

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))