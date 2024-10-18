import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())

s = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = 0

def bfs(n):
    global result
    queue = deque()
    queue.append(n)
    visited[n] = True

    while queue:
        x = queue.popleft()

        for i in s[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                result += 1




for _ in range(M):
    x,y = map(int,input().split())

    s[x].append(y)
    s[y].append(x)

bfs(1)
print(result)