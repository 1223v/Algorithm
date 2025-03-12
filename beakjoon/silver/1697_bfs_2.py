import sys
from collections import deque
input = sys.stdin.readline


N,K = map(int,input().split())
min_value = float('inf')
def bfs(n):
    global min_value
    queue = deque()
    queue.append((n,0))
    visited =[False] * (100001)
    visited[n] = True

    while queue:
        x,cost = queue.popleft()
        if x == K:
            min_value = min(cost,min_value)
        if 0 <= x*2 <= 100000:
            if not visited[x*2]:
                visited[x*2] = True
                queue.append((x*2,cost+1))
        if 0 <= x+1 <= 100000:
            if not visited[x+1]:
                visited[x+1] = True
                queue.append((x+1,cost+1))

        if 0 <= x - 1 <= 100000:
            if not visited[x-1]:
                visited[x-1] = True
                queue.append((x-1,cost+1))


bfs(N)
print(min_value)
