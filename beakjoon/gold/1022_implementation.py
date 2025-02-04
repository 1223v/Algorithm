import sys
input = sys.stdin.readline

r1,c1,r2,c2 = map(int,input().split())

graph = [[0] * (c2-c1+1) for _ in range(r2-r1+1)]
total = (r2-r1+1) * (c2-c1+1)
di = [0,-1,0,1]
dj = [1,0,-1,0]

cnt = 1
ni,nj = 0,0
length = 1
direction = 0

while total >0:

    for _ in range(2):
        for _ in range(length):
            if r1 <= ni <= r2 and c1 <= nj <= c2:
                graph[ni-r1][nj-c1] = cnt
                total -= 1
                m = cnt
            ni += di[direction]
            nj += dj[direction]
            cnt += 1

        direction = (direction + 1) % 4
    length += 1

m_len = len(str(m))

for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(graph[i][j]).rjust(m_len), end=' ')
    print()
