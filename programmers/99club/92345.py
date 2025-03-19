from collections import deque

di = [0,0,1,-1]
dj = [1,-1,0,0]

def solution(board, aloc, bloc):
    N,M = len(board), len(board[0])
    visited = [[0] * 5 for _ in range(5)]
    def dfs(board, ci,cj, oi,oj):
        nonlocal visited
        if visited[ci][cj]:
            return 0

        count = 0
        for i in range(4):
            ni,nj = ci + di[i], cj + dj[i]
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] == 0 and board[ni][nj] == 1:
                    visited[ci][cj] = 1
                    result = dfs(board,oi,oj,ni,nj) + 1
                    visited[ci][cj] = 0
                    # 현재 저장된 값 패배인데 상대가 졌다고 하면 이기는 경우로 저장
                    if count % 2 == 0 and result % 2 == 1:
                        count = result
                    # 현재 저장된 값 패배인데 상대가 이겼다고 하면 최대한 늦게 지는 횟수 선택
                    elif count % 2 == 0 and result % 2 == 0:
                        count = max(count, result)
                    # 현재 저장된 값 승리인데 상대가 졌다고 하면 최대한 빨리 이기는 횟수 선택
                    elif count % 2 == 1 and result % 2 == 1:
                        count = min(count, result)
        return count





    return dfs(board,aloc[0],aloc[1],bloc[0],bloc[1])

print(solution([[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]],
               [1, 0],
               [1, 2]))
