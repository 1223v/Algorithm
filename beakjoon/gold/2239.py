import sys
input = sys.stdin.readline

def row_chk(nr,num):
    for i in range(9):
        if graph[nr][i] == num:
            return False

    return True


def col_chk(nc, num):
    for i in range(9):
        if graph[i][nc] == num:
            return False

    return True



def three_chk(nr, nc, num):

    nr = (nr // 3) * 3
    nc = (nc // 3) * 3

    for i in range(3):
        for j in range(3):
            if graph[nr + i][nc + j] == num:
                return False

    return True

def dfs(depth):

    if depth >= len(tlst):
        for k in range(9):
            print(''.join(map(str,graph[k])))

        exit()

    nr,nc = tlst[depth]

    for i in range(1,10):
        if row_chk(nr,i) and col_chk(nc, i) and three_chk(nr, nc, i):
            graph[nr][nc] = i
            dfs(depth+1)
            graph[nr][nc] = 0




tlst = []
graph = []
for i in range(9):
    temp = list(map(int,input().rstrip()))
    for j in range(9):
        if temp[j] == 0:
            tlst.append((i,j))
    graph.append(temp)

dfs(0)
