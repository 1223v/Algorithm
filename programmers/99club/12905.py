def solution(board):


    N = len(board)
    M = len(board[0])



    for i in range(1,N):
        for j in range(1,M):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j],board[i][j-1], board[i-1][j-1]) + 1


    answer = max(map(max, board))


    return answer * answer

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))