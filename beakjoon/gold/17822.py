import sys
from copy import deepcopy
from collections import defaultdict
input = sys.stdin.readline
di,dj = [1,-1,0,0],[0,0,1,-1]
N,M,T = map(int,input().split())

graph = [[0]*M] + [list(map(int,input().split())) for _ in range(N)]


commands = []
for _ in range(T):
    x,d,k = map(int,input().split())
    commands.append((x,d,k))


# d = 0 : 시계 , d = 1 : 반시계
# k = 칸
# x = 배수인 원판들 다 회전
# 번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다.
# di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향이다.
def rotation_circle(arr,d,k):
    tmp = [0] * M

    if d == 1:
        for i in range(M):
            tmp[i] = arr[(i+k)%M]

    else:
        for i in range(M-1,-1,-1):
            tmp[i] = arr[(i-k)%M]



    return tmp

def find_value():
# 원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다.
    chk = True
    tmp_graph = [[0]*M for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(M):
            for d in range(4):
                ni,nj = i + di[d], (j + dj[d]) % M
                if 0 < ni <= N and 0 <= nj:
                    if graph[i][j] == graph[ni][nj] and graph[i][j] != 0:
                        #print("같은 수 좌표: ",i,j,ni,nj)
                        tmp_graph[i][j] = 1
                        tmp_graph[ni][nj] = 1
                        chk = False

    if chk:
        #print("원판에 같은값 존재X")
        total = 0
        cnt = 0
        for i in range(1,N+1):
            for j in range(M):
                if graph[i][j] != 0:
                    total += graph[i][j]
                    cnt += 1
        #print("평균ㅣ",total,cnt)
        if total <= 0:
            return
        avg = total / cnt

        for i in range(1, N + 1):
            for j in range(M):
                if graph[i][j] != 0:
                    if graph[i][j] > avg:
                        graph[i][j] -= 1
                    elif graph[i][j] < avg:
                        graph[i][j] += 1

    else:
        #print("원판에 같은값 존재")
        for i in range(1,N+1):
            for j in range(M):
                if tmp_graph[i][j] == 1:
                    graph[i][j] = 0



asd= 0
for x,d,k in commands:
    #print(asd)
    for i in range(1,N+1):
        if i % x == 0:
            tmp_arr = rotation_circle(graph[i],d,k)
            graph[i] = tmp_arr
    #print("회전만")
    # for i in range(1, N + 1):
    #     print(*graph[i])
    # print()
    find_value()
    # for i in range(1, N + 1):
    #     print(*graph[i])
    # print()
    asd+=1

result = 0
for i in range(1,N+1):
    result += sum(graph[i])
    #print(*graph[i])

print(result)