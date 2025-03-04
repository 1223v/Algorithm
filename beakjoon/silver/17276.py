import sys
input = sys.stdin.readline
from copy import deepcopy

TC = int(input())

def minus_sol45(tmp_graph):
    global graph
    tmp_chk = deepcopy(tmp_graph)
    tmp = deepcopy(tmp_graph)
    for i in range(N):
        tmp1 = tmp_chk[i][i]
        tmp2 = tmp_chk[i][N // 2]
        tmp3 = tmp_chk[N // 2][i]
        tmp4 = tmp_chk[i][-(1 + i)]
        tmp3_2 = tmp_chk[N // 2][-(1 + i)]

        tmp[i][i] = tmp2
        tmp[N//2][i] = tmp1
        tmp[i][N//2] = tmp4
        tmp[i][-(1 + i)] = tmp3_2

    graph = tmp[::]

def plus_sol45(tmp_graph):
    global graph
    tmp_chk = deepcopy(tmp_graph)
    tmp = deepcopy(tmp_graph)
    for i in range(N):

        tmp1 = tmp_chk[i][i]
        tmp2 = tmp_chk[i][N//2]
        tmp3 = tmp_chk[N//2][i]
        tmp4 = tmp_chk[i][-(1+i)]
        tmp3_2 = tmp_chk[N//2][-(1+i)]


        tmp[i][i] = int(tmp3)
        tmp[i][-(1 + i)] = int(tmp2)
        tmp[N // 2][-(1 + i)] = int(tmp4)
        tmp[i][N // 2] = int(tmp1)


    graph = tmp[::]




for _ in range(TC):
    N, D = map(int,input().split())

    graph = [list(map(int,input().split())) for _ in range(N)]

    if D == -45:
        minus_sol45(graph)


    elif D == -90:
        minus_sol45(graph)
        minus_sol45(graph)

    elif D == -135:
        minus_sol45(graph)
        minus_sol45(graph)
        minus_sol45(graph)

    elif D == -180:

        minus_sol45(graph)
        minus_sol45(graph)
        minus_sol45(graph)
        minus_sol45(graph)


    elif D == -225:
        minus_sol45(graph)
        minus_sol45(graph)
        minus_sol45(graph)
        minus_sol45(graph)
        minus_sol45(graph)

    elif D == -270:
        minus_sol45(graph)
        minus_sol45(graph)
        minus_sol45(graph)
        minus_sol45(graph)
        minus_sol45(graph)
        minus_sol45(graph)



    elif D == -315:
        minus_sol45(graph)
        minus_sol45(graph)
        minus_sol45(graph)
        minus_sol45(graph)
        minus_sol45(graph)
        minus_sol45(graph)
        minus_sol45(graph)

    elif D == 45:
        plus_sol45(graph)


    elif D == 90:
        plus_sol45(graph)
        plus_sol45(graph)

    elif D == 135:
        plus_sol45(graph)
        plus_sol45(graph)
        plus_sol45(graph)

    elif D == 180:

        plus_sol45(graph)
        plus_sol45(graph)
        plus_sol45(graph)
        plus_sol45(graph)


    elif D == 225:
        plus_sol45(graph)
        plus_sol45(graph)
        plus_sol45(graph)
        plus_sol45(graph)
        plus_sol45(graph)

    elif D == 270:
        plus_sol45(graph)
        plus_sol45(graph)
        plus_sol45(graph)
        plus_sol45(graph)
        plus_sol45(graph)
        plus_sol45(graph)



    elif D == 315:
        plus_sol45(graph)
        plus_sol45(graph)
        plus_sol45(graph)
        plus_sol45(graph)
        plus_sol45(graph)
        plus_sol45(graph)
        plus_sol45(graph)




    for i in range(N):
        print(' '.join(map(str, graph[i])))