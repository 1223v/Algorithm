import sys
input = sys.stdin.readline
from collections import deque
N = int(input())

graph = [[] for _ in range(N**2+1)]
tbl = [[0] * N for _ in range(N)]
di,dj = [1,-1,0,0],[0,0,1,-1]
start = deque()
for _ in range(N**2):
    s, a,b,c,d = map(int,input().split())
    graph[s].extend([a,b,c,d])
    start.append(s)




for s in start:
    tmp = []
    for i in range(N):
        for j in range(N):
            f_value, bin_value = 0,0
            for k in range(4):

                ni,nj = i + di[k], j + dj[k]

                if 0 <= ni < N and 0 <= nj < N:
                    # 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
                    if tbl[ni][nj] == 0:
                        bin_value += 1

                    # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
                    elif tbl[ni][nj] in graph[s]:
                        f_value += 1

            tmp.append((f_value,bin_value,i,j))

    # 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
    tmp.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    # 조건에 맞게 자리 앉히기

    for i in tmp:
        if tbl[i[2]][i[3]] == 0:
            tbl[i[2]][i[3]] = s
            break



result = 0
# 좋아하는 학생이 주변에 몇명인지 확인


for i in range(N):
    for j in range(N):
        f_value = 0
        for k in range(4):
            ni,nj = i + di[k], j + dj[k]

            if 0 <= ni < N and 0 <= nj < N:
                if tbl[ni][nj] in graph[tbl[i][j]]:
                    f_value += 1

        if f_value == 0:

            result += f_value
        elif f_value == 1:
            result += f_value

        elif f_value == 2:
            result += 10

        elif f_value == 3:
            result += 100

        elif f_value == 4:
            result+= 1000

print(result)
