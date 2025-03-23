import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]
di,dj = [0,1,0,-1],[-1,0,1,0]


dr = 0
ans= 0
ai = [[-2,-1,-1,-1,0,1,1,1,2,0],
      [0,1,0,-1,2,1,0,-1,0,1],
      [2,1,1,1,0,-1,-1,-1,-2,0],
      [0,-1,0,1,-2,-1,0,1,0,-1],
]

aj = [[0,-1,0,1,-2,-1,0,1,0,-1],
      [-2,-1,-1,-1,0,1,1,1,2,0],
      [0,1,0,-1,2,1,0,-1,0,1],
      [2,1,1,1,0,-1,-1,-1,-2,0]
]
avg = [2,10,7,1,5,10,7,1,2,0]
def toneido():
    global dr
    ci, cj = N // 2, N // 2
    max_cnt = 1
    cnt = 0
    flag = 0
    while (ci,cj) != (0,0):
        ci, cj = ci + di[dr], cj + dj[dr]

        if graph[ci][cj] > 0:
            sand_count(ci,cj)

        cnt += 1
        if cnt == max_cnt:
            cnt = 0
            dr = (dr+1) %4
            if flag == 0:
                flag = 1

            else:
                flag = 0
                max_cnt += 1


def sand_count(i,j):
    global ans
    val = graph[i][j]
    graph[i][j] = 0
    sm = 0
    for k in range(10):
        ni,nj = i+ai[dr][k],j + aj[dr][k]
        t = (val * avg[k])// 100
        if k==9:
            t = val - sm
        if 0 <= ni < N and 0 <= nj < N:
            graph[ni][nj] += t

        else:
            ans += t
        sm += t


toneido()
print(ans)