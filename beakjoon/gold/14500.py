import sys
input = sys.stdin.readline

N, M = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]

block = [
    # 회전
    ((0,0),(0,1),(0,2),(0,3)),((0,0),(1,0),(2,0),(3,0)),
    ((0,0),(0,1),(1,0),(1,1)),
    ((0,0),(0,-1),(0,1),(-1,0)),((0,0),(0,-1),(0,1),(1,0)),((0,0),(1,0),(-1,0),(0,-1)),((0,0),(1,0),(-1,0),(0,1)),
    ((0,0),(0,1),(-1,0),(-2,0)),((0,0),(0,1),(0,2),(1,0)),((0,0),(0,-1),(1,0),(2,0)),((0,0),(-1,0),(0,-1),(0,-2)),
    ((0,0),(-1,0),(0,1),(1,1)),((0,0),(0,1),(1,0),(1,-1)),
    # 대칭
    ((0,0),(0,-1),(-1,0),(-2,0)),((0,0),(-1,0),(0,1),(0,2)), ((0,0),(0,1),(1,0),(2,0)), ((0,0),(1,0),(0,-1),(0,-2)),
    ((0,0),(0,1),(-1,1),(1,0)),((0,0),(0,-1),(1,0),(1,1)) # z
]

max_value = 0
for i in range(N):
    for j in range(M):

        for point1, point2, point3, point4 in block:
            tmp = 0
            point1_i,point1_j = i+point1[0],j+point1[1]
            point2_i, point2_j = i + point2[0], j + point2[1]
            point3_i, point3_j = i + point3[0], j + point3[1]
            point4_i, point4_j = i + point4[0], j + point4[1]

            if (0 <= point1_i < N and 0 <= point1_j < M) and (0 <= point2_i < N and 0 <= point2_j < M) and (0 <= point3_i < N and 0 <= point3_j < M) and (0 <= point4_i < N and 0 <= point4_j < M):

                tmp = graph[point1_i][point1_j] + graph[point2_i][point2_j] + graph[point3_i][point3_j] + graph[point4_i][point4_j]
                # print(tmp, point1_i,point1_j, point2_i,point2_j, point3_i,point3_j, point4_i,point4_j)
                max_value = max(tmp,max_value)
print(max_value)
