import sys
from collections import deque
input = sys.stdin.readline

TC = int(input())

di = [-1,-2,-2,-1,1,2,2,1]
dj = [-2,-1,1,2,-2,-1,1,2]

for _ in range(TC):
    N = int(input())
    s = [[-1] * N for _ in range(N)]

    x1,y1 = map(int,input().split())
    x2, y2 = map(int, input().split())



    def bfs(x1,y1):
        queue = deque()
        queue.append((x1,y1))
        s[x1][y1] = 0

        while queue:
            if s[x2][y2] != -1:
                break
            ci,cj = queue.popleft()
            for i in range(8):
                ni, nj = ci+di[i], cj+dj[i]
                if 0 <= ni < N and 0 <= nj < N and s[ni][nj] == -1:
                    s[ni][nj] = s[ci][cj] + 1
                    queue.append((ni,nj))


        print(s[x2][y2])

    bfs(x1,y1)