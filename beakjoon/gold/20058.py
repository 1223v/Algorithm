import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

N,Q = map(int,input().split())
total_N = 2**N

di,dj = [-1,1,0,0],[0,0,-1,1]
graph = [list(map(int,input().split())) for _ in range(total_N)]
visited = [[0] * total_N for _ in range(total_N)]
commands = list(map(int,input().split()))

def rotation_board(L):

    total_L = 2**L
    tmp = deepcopy(graph)

    tmp_value = 0
    for k in range(total_L,total_N+1, total_L):
        for i in range(tmp_value,k):
            for j in range(tmp_value,k):
                tmp[j][k-1-i] = graph[i][j]
        tmp_value = k

    return tmp



def melt_ice(tmp_graph):
    demo_graph = [[0] * total_N for _ in range(total_N)]
    for i in range(total_N):
        for j in range(total_N):

            cnt = 0
            for d in range(4):
                ni,nj = i + di[d], j + dj[d]
                if 0<= ni < total_N and 0 <= nj < total_N:
                    if tmp_graph[ni][nj] > 0:
                        cnt += 1
            if cnt < 3:
                demo_graph[i][j] += 1


    for i in range(total_N):
        for j in range(total_N):
            if tmp_graph[i][j] > demo_graph[i][j]:
                tmp_graph[i][j] -= demo_graph[i][j]
            else:
                tmp_graph[i][j] = 0

    return tmp_graph



def check_size(i,j):
    queue =deque()

    queue.append((i,j))
    visited[i][j] = 1
    ice_count = 1

    while queue:
        ci,cj = queue.popleft()

        for i in range(4):
            ni,nj = ci + di[i],cj + dj[i]
            if 0 <= ni < total_N and 0 <= nj < total_N:
                if visited[ni][nj] == 0 and graph[ni][nj] > 0:
                    visited[ni][nj] = 1
                    queue.append((ni,nj))
                    ice_count += 1

    return ice_count

for L in commands:


    tmp_graph = rotation_board(L)
    graph = melt_ice(tmp_graph)

result = 0
max_value = 0
for i in range(total_N):
    for j in range(total_N):
        result += graph[i][j]
        if visited[i][j] == 0 and graph[i][j] > 0:
            max_value = max(check_size(i,j),max_value)

print(result)
print(max_value)