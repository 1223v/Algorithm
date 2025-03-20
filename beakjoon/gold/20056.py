import sys
input = sys.stdin.readline
from copy import deepcopy

N,M,K = map(int,input().split())
di,dj = [-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]
graph = [[[] for _ in range(N)] for _ in range(N)]
tmp = [[[] for _ in range(N)] for _ in range(N)]
f_lst = []
for _ in range(M):
    r,c,m,s,d = map(int,input().split())
    graph[r-1][c-1].append((m,s,d))


for cnt in range(K):

    # 이동
    for i in range(N):
        for j in range(N):
            for _ in range(len(graph[i][j])):
                m,s,d = graph[i][j].pop()
                ni,nj = (i + di[d]* s ) % N, (j+ dj[d] * s) %N


                tmp[ni][nj].append((m,s,d))

    graph=deepcopy(tmp)
    tmp = [[[] for _ in range(N)] for _ in range(N)]


    # 2개 이상의 파이어볼이 있는 칸
    # 같은 칸에 있는 파이어볼은 모두 하나로 합
    tmp = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) > 1:
                check = True
                total_m = 0
                total_s = 0
                total_cnt = len(graph[i][j])
                total_d = graph[i][j][0][2]

                for m,s,d in graph[i][j]:
                    total_m += m
                    total_s += s
                    if d % 2 != total_d % 2:
                        check = False


                result_m, result_s = int(total_m / 5), int(total_s / total_cnt)

                if result_m > 0:

                    if check:
                        tmp[i][j].append((result_m, result_s,0))
                        tmp[i][j].append((result_m, result_s, 2))
                        tmp[i][j].append((result_m, result_s, 4))
                        tmp[i][j].append((result_m, result_s, 6))
                    else:
                        tmp[i][j].append((result_m, result_s, 1))
                        tmp[i][j].append((result_m, result_s, 3))
                        tmp[i][j].append((result_m, result_s, 5))
                        tmp[i][j].append((result_m, result_s, 7))

                graph[i][j] = tmp[i][j]

    tmp = [[[] for _ in range(N)] for _ in range(N)]





result = 0
for i in range(N):
    for j in range(N):

        if len(graph[i][j]) > 0:
            for m,s,d in graph[i][j]:
                result += m



print(result)







