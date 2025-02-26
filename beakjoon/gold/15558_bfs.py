import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int,input().split())

# 0 = 불가 1 = 가능한 칸
graph = [[1]*200000 for _ in range(2)]

for i in range(2):
    s = input().rstrip()
    for j in range(N):

        graph[i][j] = int(s[j])


chk = False

def bfs():
    global chk

    queue = deque()
    visited = [[0] * 200000 for _ in range(2)]

    visited[0][0] = 1

    queue.append((0,0,0,0))


    while queue:
        ci,cj,total,time = queue.popleft()
        #print(ci,cj,total,time)

        #print(total,N)
        if total > N-1:
            print(1)
            exit()
        ni1,nj1 = ci, cj+1
        ni2,nj2 = ci, cj-1
        ni3,nj3 = ci + 1, cj + K
        ni4, nj4 = ci - 1, cj + K

        if 0 <= ni1 < 2 and 0 <= nj1 < 200000:
            if nj1 > time and graph[ni1][nj1] == 1 and not visited[ni1][nj1]:
                visited[ni1][nj1] = 1
                queue.append((ni1,nj1,total+1, time+1))
        if 0 <= ni2 < 2 and 0 <= nj2< 200000:
            if nj2 > time and graph[ni2][nj2] == 1 and not visited[ni2][nj2]:
                visited[ni2][nj2] = 1
                queue.append((ni2, nj2, total - 1, time + 1))
        if 0 <= ni3 < 2 and 0 <= nj3< 200000:
            if nj3 > time and graph[ni3][nj3] == 1 and not visited[ni3][nj3]:
                visited[ni3][nj3] = 1
                queue.append((ni3, nj3, total + K, time + 1))
        if 0 <= ni4 < 2 and 0 <= nj4< 200000:
            if nj4 > time and graph[ni4][nj4] == 1 and not visited[ni4][nj4]:
                visited[ni4][nj4] = 1
                queue.append((ni4, nj4, total + K, time + 1))

bfs()
if chk:
    print(1)

else:
    print(0)
