import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)
distance = [0] * (N+1)

for _ in range(N):
    numbers = list(map(int, input().split()))
    index= 0
    s = numbers[index]
    index += 1
    while True:
        u = numbers[index]
        if u == -1:
            break
        v = numbers[index+1]
        index += 2


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in A[x]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[x] + i[1]

bfs(1)
print(max(distance))
