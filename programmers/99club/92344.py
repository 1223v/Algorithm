def solution(board, skill):
    answer = 0

    M, N = len(board[0]),len(board)
    tile = [[0 for _ in range(M+1)] for _ in range(N+1)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            tile[r1][c1] += (-degree)
            tile[r2+1][c2+1] += (-degree)
            tile[r1][c2+1] -= (-degree)
            tile[r2+1][c1] -= (-degree)

        else:
            tile[r1][c1] += degree
            tile[r2+1][c2+1] += degree
            tile[r1][c2+1] -= degree
            tile[r2+1][c1] -= degree


    for i in range(N+1):
        for j in range(1,M+1):
            tile[i][j] += tile[i][j-1]

    for i in range(M+1):
        for j in range(1,N+1):
            tile[j][i] += tile[j-1][i]

    for i in range(N):
        for j in range(M):
            if board[i][j] + tile[i][j] > 0:
                answer += 1

    print(answer)

    return answer