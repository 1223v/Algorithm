import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]
dict = [0] * (N+1)
result = []
def bfs():
    queue = deque()
    for i in range(1,N+1):
        if dict[i] == 0:
            queue.append(i)

    while queue:
        x = queue.popleft()
        result.append(x)
        for i in graph[x]:
            dict[i] -= 1
            if dict[i] == 0 and i != 0:
                queue.append(i)


for _ in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)
    dict[e] += 1

bfs()
print(*result)
