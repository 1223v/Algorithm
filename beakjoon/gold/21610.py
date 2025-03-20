import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
di,dj = [0,-1,-1,-1,0,1,1,1],[-1,-1,0,1,1,1,0,-1]
commands = []
for _ in range(M):
    d,s = map(int,input().split())
    commands.append((d-1,s))


def move_cloud(cloud, d, s):

    water_re_pos = []
    for i,j in cloud:
        ni, nj = (i + di[d] * s) % N, (j + dj[d] * s) % N
        graph[ni][nj] += 1
        water_re_pos.append((ni,nj))
        visited[ni][nj] = 1

    for ci,cj in water_re_pos:
        cnt = 0
        for i in [1,3,5,7]:
            ni,nj = ci + di[i], cj + dj[i]
            if 0 <= ni < N and 0 <= nj < N:
                if graph[ni][nj] > 0:
                    cnt += 1
        graph[ci][cj] += cnt




def create_cloud(visited):

    tmp_cloud = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2 and visited[i][j] == 0:
                tmp_cloud.append((i,j))
                graph[i][j] -= 2


    return tmp_cloud






cloud = [(N-1,0), (N-1,1),(N-2,0),(N-2,1)]
for d,s in commands:
    visited = [[0] * N for _ in range(N)]
    move_cloud(cloud, d, s)

    cloud = create_cloud(visited)

result = 0
for i in range(N):
    result += sum(graph[i])

print(result)




