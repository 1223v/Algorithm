
result = []
di,dj = [1,0,-1,0],[0,1,0,-1] # 하,우, 상, 좌
def turn_board(graph,i1,j1,i2,j2):
    tmp_graph = graph

    first_value = graph[i1][j1]
    ni,nj = i1,j1
    min_value = graph[ni][nj]
    dr = 0

    while not(i1 == ni and j1+1 == nj):

        ci,cj = ni,nj
        ni,nj = ni + di[dr], nj + dj[dr]


        if i1 <= ni <= i2 and j1 <= nj <= j2:

            tmp_graph[ci][cj] = tmp_graph[ni][nj]
            min_value = min(min_value, tmp_graph[ni][nj])

        else:
            ni, nj =ci,cj

            dr = (dr + 1) % 4



    tmp_graph[i1][j1+1]= first_value

    result.append(min_value)


    return tmp_graph


def solution(rows, columns, queries):

    graph = [[0] * columns for _ in range(rows)]

    c = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = c
            c += 1



    for i1,j1,i2,j2 in queries:
        graph = turn_board(graph,i1-1,j1-1,i2-1,j2-1)

    return result

print(solution(3,3	,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))