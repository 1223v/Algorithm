import sys
input = sys.stdin.readline

N, M, H = map(int,input().split())
board = [[0] * (N+2) for _ in range(H+1)]
for _ in range(M):
    a,b = map(int,input().split())
    board[a][b] = 1

pos = []
for i in range(1,H+1):
    for j in range(1, N+1):
        if board[i][j] == 0:
            pos.append((i,j))

CNT = len(pos)

def check():
    for j in range(1,N+1):
        sj = j
        for i in range(1,H+1):
            if board[i][sj-1] == 1:
                sj -= 1

            elif board[i][sj] == 1:
                sj += 1
        if sj != j:
            return False
    return True


def dfs(n, s):
    global ans
    if ans == 1:
        return
    if n == cnt:
        if check():
            ans = 1
        return

    for i in range(s, CNT):
        ci,cj = pos[i]
        if board[ci][cj -1] == 0 and board[ci][cj+1] == 0:
            board[ci][cj] = 1
            dfs(n+1, i+1)
            board[ci][cj] = 0

for cnt in range(4):
    ans = 0
    dfs(0,0)

    if ans == 1:
        ans = cnt
        break

else:
    ans = -1

print(ans)
