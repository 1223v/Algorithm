import sys
from collections import deque
input = sys.stdin.readline

# 층수, 현재 위치, 목적지, 업, 다운
F, S, G, U, D = map(int,input().split())
count = 0
visited = [-1] * (F+1)
def bfs(start):
    queue = deque()


    queue.append(start)
    visited[start] += 1

    while queue:
        x = queue.popleft()

        for i in [(U),(-D)]:
            if 1 <= x+i <= F:
                if visited[x+i] == -1:
                    visited[x+i] = visited[x] + 1
                    queue.append(x+i)


bfs(S)

if visited[G] >= 0:

    print(visited[G])
else:
    print("use the stairs")
